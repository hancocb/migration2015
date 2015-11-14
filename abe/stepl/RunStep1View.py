from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from templatetags.simple_tags import twonum
from tools import extract
from utils import requests
import json

class RunStep1View(View):
    
    def post(self, request, *args, **kwargs):

        #all saved to session
        context = request.session
        session_id=context['IndexInput']['id']
        #process inputs from bmpMain

        #process landtype_id: 1~5 : Cropland, pastland, forest,user defined,feedlot
        for landtype_id in range(1,6):
            for watershd_id in context['rangeWSD']:
                if not BMPInput.objects.filter(session_id=session_id, landtype_id=landtype_id ,
                    watershd_id=watershd_id).exists():
                    bmpInput = BMPInput(
                        session_id=session_id, 
                        landtype_id=landtype_id,
                        watershd_id=watershd_id
                        )
                else:
                    bmpInput = BMPInput.objects.get(session_id=session_id, landtype_id=landtype_id, 
                        watershd_id=watershd_id)
                bmpInput.BMP = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"5"]
                bmpInput.PercentApplied=request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"6"]
                bmpInput.N   = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"1"]
                bmpInput.P   = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"2"]
                bmpInput.BOD = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"3"]
                bmpInput.Sediment=request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"4"]
                bmpInput.save()

        #UrbnConc
        for i in range(1,5):
            for j in range(1,10):
                key = "UrbnConc_"+str(i)+str(j)
                if not UrbanBmpInput.objects.filter(session_id=session_id, key=key).exists():
                    urbanBmpInput = UrbanBmpInput(
                        session_id=session_id, 
                        key=key
                        )
                else:
                    urbanBmpInput = UrbanBmpInput.objects.get(session_id=session_id, key=key)
                urbanBmpInput.value = request.POST[key]
                urbanBmpInput.save()

        #UrbanBMP_
        for k in context['range5']:
            for i in context['rangeWSD']:
                for j in context['range9']: 
                    key = 'UrbanBMP_'+str(k)+'_'+twonum(i)+str(j) 
                    if not UrbanBmpInput.objects.filter(session_id=session_id, key=key).exists():
                        urbanBmpInput = UrbanBmpInput(
                            session_id=session_id, 
                            key=key
                            )
                    else:
                        urbanBmpInput = UrbanBmpInput.objects.get(session_id=session_id, key=key)
                    urbanBmpInput.value = request.POST[key]
                    urbanBmpInput.save()

        #process through STPEL api to run fortran
        from_id = URL_RUN_FROM_ID + str(session_id)
        run1_url = FORTRAN_SERVER + URL_RUN_STEP_1
        text = self.runStep1(context,from_id,run1_url)
        print text

        #parse text
        ret = json.loads(text);
        clmArr = [0,1,3,4,5,7,8,9,11,12,13,15,16]
        img_prefix = FORTRAN_SERVER + "tmp/" + from_id + "/" 

        return render(request, 'runStep1.html', { 
            'ctx':context, 'req' : request, 'run1ret':ret['run1ret'][1:], 
            'img_prefix' : img_prefix, 'clmArr':clmArr
            })

    def get(self, request):
        raise Http404("GET of this page does not exist, you need POST")

    def runStep1(self, context, from_id, run1_url):

        Gully       = self.getGully(context)
        WildLife    = self.getWildLife(context)
        Reference   = self.getReference(context)
        Feedlot     = self.getFeedlot(context)
        pcp         = self.getpcp(context)
        mainINP     = self.getmainINP(context)
        Septic      = self.getSeptic(context)
        LandRain_GW1 = self.getLandRain_GW1(context)
        BMPs        = self.getBMPs(context)

        #URL_RUN_STEP_1 is from stepl_setting
        data={
            "Gully.txt":Gully,      'WildLife.txt':WildLife,        "Reference.txt" : Reference,
            "Feedlot.txt":Feedlot,                                  "mainINP.txt" : mainINP,
            "Septic.txt":Septic,    'LandRain_GW1.txt':LandRain_GW1, "BMPs.txt" : BMPs,
            }

        data['pcp_FileName'] = pcp['FileName']
        data['pcp_stateN'] = pcp['stateN']
        data['pcp_countyN'] = pcp['countyN']
        data['pcp_stationN'] = pcp['stationN']
        data['from_id'] = from_id

        ret = requests.post(run1_url,data = data)
        return ret.text

    def getGully(self, context):
        session_id=context['IndexInput']['id']

        #do the inverse things as in importData.py
        #Gully.txt
        Gully = "";
        for i in range(1,11):
            textureClass = Soil_Textural_Class_Choices[i-1][1]
            s = SoilTextureInput.objects.get(session_id=session_id,Soil_Textural_Class=textureClass)
            gullyDB_1 = '%.4f' % s.Dry_Density 
            gullyDB_2 = '%.4f' % s.Correction_Factor 
            Gully += gullyDB_1 + '\t' + gullyDB_2 + '\t\n'
        Gully += '-----------------------\n'

        g1 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Slight')
        g2 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Moderate')
        g3 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Severe')
        g4 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Very Severe')
        Gully += '%.4f' % g1.Medium_Value + "\n" + '%.4f' % g2.Medium_Value + "\n"
        Gully += '%.4f' % g3.Medium_Value + "\n" + '%.4f' % g4.Medium_Value + "\n"
        Gully += '-----------------------\n'

        indexInput = IndexInput.objects.get(id=session_id)
        Gully += str(indexInput.num_gully) + "\n"
        GullyErosionInput_map = [
              '',
              'watershd_id', 
              'Gully_id', 
              'Top_Width', 
              'Bottom_Width', 
              'Depth', 
              'Length', 
              'Years_to_Form', 
              'BMP_Efficiency', 
              'SoilTexture', 
        ]
        for i in context['rangeGLY']:
            g = GullyErosionInput.objects.get(session_id=session_id,Gully_id=i)
            for j in range(1,10):
                Gully += str(getattr(g,GullyErosionInput_map[j])) + "\t"
            Gully += "\n"    
        Gully += '-----------------------\n'

        Gully += str(indexInput.num_steambank) + "\n"
        StreambankErosionInput_map = [
              '',
              'watershd_id', 
              'Streambank_id', 
              'Length', 
              'Height', 
              'Lateral_Recession', 
              'BMP_Efficiency', 
              'SoilTexture', 
        ]
        for i in context['rangeSTR']:
            g = StreambankErosionInput.objects.get(session_id=session_id,Streambank_id=i)
            for j in range(1,8):
                Gully += str(getattr(g,StreambankErosionInput_map[j])) + "\t"
            Gully += "\n"    
        
        return Gully


    def getWildLife(self, context):
        session_id=context['IndexInput']['id']

        #WildLife.txt
        WildLife = ""
        keyMap = ['Goose','Deer','Beaver','Raccoons','Other']
        for key in keyMap:
            w = WildlifeDensityInCropLandInput.objects.get(session_id=session_id,Wildlife=key)
            WildLife += str( '%.2f' % w.NumPerMileSquare) + "\n"

        return WildLife


    def getReference(self, context):
        session_id=context['IndexInput']['id']

        #Reference.txt
        Reference = 'Typical Animal Mass,lb  BOD,lb/day/1000lb animal        BOD per Animal,lb/day   BOD per Animal,lb/yr \n'
        Animals = ['','Beef cattle','Dairy cow','Hog','Sheep','Horse','Chicken (Layer)','Turkey','Duck','Goose','Deer','Beaver','Raccoon','Other',]
        for i in range(1,14):
            Animal = Animals[i]
            r = AnimalWeightInput.objects.get(session_id=session_id,Animal=Animal)
            Reference += '%.2f' % r.MassLb + "\t"
            Reference += '%.2f' % r.BOD_per_1000lb + "\t"
            Reference += '%.2f' % r.BOD_per_day + "\t"
            Reference += '%.2f' % r.BDO_per_year + "\t"
            Reference += "\n"
        
        return Reference

    def getFeedlot(self, context):
        session_id=context['IndexInput']['id']

        #Feedlot.txt
        Feedlot = 'N\tP\tBOD\tCOD\tAnimal\n'
        Animals = ['','Slaughter Steer','Young Beef','Dairy Cow','Young Dairy Stock','Swine','Feeder Pig','Sheep','Horse','Chicken','Turkey','Duck']
        for i in range(1,12):
            Animal = Animals[i]
            r = FeedlotAnimalInput.objects.get(session_id=session_id,Animal=Animal)
            Feedlot += '%.3f' % r.N + "\t"
            Feedlot += '%.3f' % r.P + "\t"
            Feedlot += '%.3f' % r.BOD + "\t"
            Feedlot += '%.3f' % r.COD + "\t"
            Feedlot += "\n"

        return Feedlot

    def getpcp(self, context):
        session_id=context['IndexInput']['id']        
        #pcp.txt -- pass to generate pcp.txt
        #LocFileName-->myFile = str(form.getvalue('FileName'))
        #State-->stateN = str(form.getvalue('stateN'))
        #CountyName-->countyN = str(form.getvalue('countyN'))
        #LocName-->stationN = str(form.getvalue('stationN'))
        c = CountyDataInput.objects.get(session_id=session_id)
        pcp = {
            'FileName': c.LocFileName,
            'stateN': c.state_name,
            'countyN': c.name,
            'stationN': c.LocName,
        }

        return pcp

    def getmainINP(self, context):
        session_id=context['IndexInput']['id']  
        #mainINP.txt
        mainINP = ""
        indexInput = IndexInput.objects.get(id=session_id)
        mainINP += str(indexInput.num_watershd) + "\t"
        if indexInput.swsOpt :
            mainINP += "1\n"
        else:
            mainINP += "4\n"
        mainINP += '----------------------------------------------------\n'
            
        #table 1
        for watershd_id in context['rangeWSD'] :
            watershedLandUse = WatershedLandUse.objects.get(session_id=session_id, watershd_id=watershd_id)
            for i in range(1,7):
                num = '%.2f' % getattr( watershedLandUse,WatershedLandUse_index_map[i]) + "\t"
                mainINP += num 
            # watershedLandUse.HSG is not used here, for with SoilDataInput
            mainINP += '%.2f' % watershedLandUse.FeedlotPercentPaved + "\t"
            mainINP += '%.2f' % watershedLandUse.Total + "\n"
        mainINP += '----------------------------------------------------\n'

        #table 2
        for watershd_id in context['rangeWSD'] :
            agriAnimal = AgriAnimal.objects.get(session_id=session_id, watershd_id=watershd_id)
            for i in range(1,9):
                num = str( getattr( agriAnimal,AgriAnimal_index_map[i]) ) + "\t"
                mainINP += num    
            mainINP += str(agriAnimal.numMonthsManureApplied) + "\t"
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'

        #table 3
        for watershd_id in context['rangeWSD'] :
            ele = SepticNillegal.objects.get(session_id=session_id, watershd_id=watershd_id)
            mainINP += '%.2f' % ele.numSepticSystems + "\t" #NumSpSys
            mainINP += '%.2f' % ele.PopulationPerSeptic + "\t" #PpSpSys
            mainINP += '%.2f' % ele.SepticFailureRate_Percent + "\t" #SpFailRate
            mainINP += '%.2f' % ele.Wastewater_Direct_Discharge_numPeople + "\t" #NumPpDrtDc
            mainINP += '%.2f' % ele.Direct_Discharge_Reduction_Percent + "\n" #RdcDrtDc
        mainINP += '----------------------------------------------------\n'

        #table 4
        for watershd_id in context['rangeWSD'] :
            ele = UniversalSoilLossEquation.objects.get(session_id=session_id, watershd_id=watershd_id)
            for i in range(1,6):
                num = '%.4f' % getattr( ele,"Cropland_"+UniversalSoilLossEquation_index_map[i]) + "\t"
                mainINP += num    
            mainINP += "\n"    

        mainINP += "\n"    
        for watershd_id in context['rangeWSD'] :
            ele = UniversalSoilLossEquation.objects.get(session_id=session_id, watershd_id=watershd_id)
            for i in range(1,6):
                num = '%.4f' % getattr( ele,"Pastureland_"+UniversalSoilLossEquation_index_map[i]) + "\t"
                mainINP += num    
            mainINP += "\n"

        mainINP += "\n"    
        for watershd_id in context['rangeWSD'] :
            ele = UniversalSoilLossEquation.objects.get(session_id=session_id, watershd_id=watershd_id)
            for i in range(1,6):
                num = '%.4f' % getattr( ele,"Forest_"+UniversalSoilLossEquation_index_map[i]) + "\t"
                mainINP += num    
            mainINP += "\n"

        mainINP += "\n"    
        for watershd_id in context['rangeWSD'] :
            ele = UniversalSoilLossEquation.objects.get(session_id=session_id, watershd_id=watershd_id)
            for i in range(1,6):
                num = '%.4f' % getattr( ele,"UserDefined_"+UniversalSoilLossEquation_index_map[i]) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'

        #table 5
        for watershd_id in context['rangeWSD'] :
            watershedLandUse = WatershedLandUse.objects.get(session_id=session_id, watershd_id=watershd_id)
            ele = SoilDataInput.objects.get(session_id=session_id, watershd_id=watershd_id)
            mainINP += str(watershedLandUse.HSG) + "\t"
            for f in SoilDataAbstract._meta.fields:
                num = '%.3f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'


        #table 6
        eles = ReferenceRunoffInput.objects.filter(session_id=session_id).order_by('id')
        for ele in eles:
            for f in RunoffAbastract._meta.fields:
                num = '%.2f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'

        #table 6a
        eles = DetailedRunoffInput.objects.filter(session_id=session_id).order_by('id')
        for ele in eles:
            for f in RunoffAbastract._meta.fields:
                num = '%.2f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'
        

        #table 7
        eles = NutrientRunoffInput.objects.filter(session_id=session_id).order_by('id')
        for ele in eles:
            for f in NutrientAbstract._meta.fields:
                num = '%.3f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'
        
        #table 7a
        eles = NutrientGroundwaterRunoffInput.objects.filter(session_id=session_id).order_by('id')
        for ele in eles:
            for f in NutrientAbstract._meta.fields:
                num = '%.3f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'
        
        #table 8
        for watershd_id in context['rangeWSD'] :
            watershedLandUse = WatershedLandUse.objects.get(session_id=session_id, watershd_id=watershd_id)
            ele = LanduseDistributionInput.objects.get(session_id=session_id, watershd_id=watershd_id)
            mainINP += str(watershedLandUse.Urban) + "\t"
            for f in LanduseDistributionAbstract._meta.fields:
                num = '%.2f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'

        #table 9 
        for watershd_id in context['rangeWSD'] :
            watershedLandUse = WatershedLandUse.objects.get(session_id=session_id, watershd_id=watershd_id)
            ele = IrrigationInput.objects.get(session_id=session_id, watershd_id=watershd_id)
            mainINP += str(watershedLandUse.Cropland) + "\t"
            for f in IrrigationAbstract._meta.fields:
                num = '%.2f' % getattr( ele,f.name) + "\t"
                mainINP += num    
            mainINP += "\n"
        mainINP += '----------------------------------------------------\n'

        return mainINP

    def getSeptic(self, context):
        session_id=context['IndexInput']['id']  
        #Septic.txt
        Septic = ""
        eles = SepticSystemInput.objects.filter(session_id=session_id).order_by('id')
        for ele in eles:
            Septic += str(ele.ACR) + "\n"
        for ele in eles:
            Septic += str(ele.Wastewater_per_capita) + "\n"    
        
        return Septic

    def getLandRain_GW1(self, context):
        session_id=context['IndexInput']['id']     
        indexInput = IndexInput.objects.get(id=session_id)

        #LandRain_GW1.txt
        LandRain_GW1 = 'A\tB\tC\tD\tSHG\n'
        eles = SoilInfiltrationFractionInput.objects.filter(session_id=session_id).order_by('id')
        for ele in eles:
            for f in SoilInfiltrationFractionAbstract._meta.fields:
                if f.name == 'HSG':
                    continue
                if indexInput.gwOpt:
                    num = '%.3f' % getattr( ele,f.name) + "\t"
                else:
                    num = '%.3f' % 0 + "\t"
                LandRain_GW1 += num    
            LandRain_GW1 += "\n"
        return LandRain_GW1

    def getBMPs(self, context):
        session_id=context['IndexInput']['id']          
        #BMPs.txt
        BMPs = ""
        #process landtype_id: 1~5 : Cropland, pastland, forest,user defined,feedlot
        for landtype_id in range(1,6):
            BMPs += '\tN\tP\tBOD\tSediment\tAppliedArea\tBMP\n'
            for watershd_id in context['rangeWSD']:
                bmpInput = BMPInput.objects.get(session_id=session_id, landtype_id=landtype_id, 
                        watershd_id=watershd_id)
                
                BMPs += '%.4f' % bmpInput.N + "\t" #= request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"1"]
                BMPs += '%.4f' % bmpInput.P + "\t"  #= request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"2"]
                BMPs += '%.4f' % bmpInput.BOD + "\t" #= request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"3"]
                BMPs += '%.4f' % bmpInput.Sediment + "\t" #=request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"4"]
                BMPs += '%.4f' % bmpInput.PercentApplied + "\t" #=request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"6"]
                BMPs += str(bmpInput.BMP) + "\n" #= request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"5"]
            if landtype_id != 5:
                BMPs += "\n"

        BMPs += '------------ Followings are BMPs for Urban-------------------------------------------------\n'
        
        import time
        time.sleep(2) # delays for 2 seconds

        for i in range(1,5):
            for j in range(1,10):
                key = "UrbnConc_"+str(i)+str(j)
                urbanBmpInput = UrbanBmpInput.objects.get(session_id=session_id, key=key)
                BMPs += '%.4f' % urbanBmpInput.value + "\t"
            BMPs += "\n"
        BMPs += "\n"

        #UrbanBMP_
        for k in context['range5']:
            for i in context['rangeWSD']:
                for j in context['range9']: 
                    key = 'UrbanBMP_'+str(k)+'_'+twonum(i)+str(j) 
                    urbanBmpInput = UrbanBmpInput.objects.get(session_id=session_id, key=key)
                    BMPs += '%.4f' % urbanBmpInput.value + "\t"
                BMPs += "\n"
            BMPs += "\n"

        return BMPs

        



