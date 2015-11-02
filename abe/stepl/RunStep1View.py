from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from templatetags.simple_tags import twonum
from tools import extract
from utils import requests

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
        ret = self.runStep1(context)

        return render(request, 'runStep1.html', { 'ctx':context, 'req' : request, 'ret':ret })

    def get(self, request):
        raise Http404("GET of this page does not exist, you need POST")

    def runStep1(self, context):
        session_id=context['IndexInput']['id']

        #do the inverse things as in importData.py
        #GuyllyDB.txt
        guyllyDB = "";
        for i in range(1,11):
            textureClass = Soil_Textural_Class_Choices[i-1][1]
            s = SoilTextureInput.objects.get(session_id=session_id,Soil_Textural_Class=textureClass)
            gullyDB_1 = '%.4f' % s.Dry_Density 
            gullyDB_2 = '%.4f' % s.Correction_Factor 
            guyllyDB += gullyDB_1 + '\t' + gullyDB_2 + '\t\n'
        guyllyDB += '-----------------------\n'

        g1 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Slight')
        g2 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Moderate')
        g3 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Severe')
        g4 = LateralRecessionRateInput.objects.get(session_id=session_id,Category='Very Severe')
        guyllyDB += '%.4f' % g1.Medium_Value + "\n" + '%.4f' % g2.Medium_Value + "\n"
        guyllyDB += '%.4f' % g3.Medium_Value + "\n" + '%.4f' % g4.Medium_Value + "\n"
        guyllyDB += '-----------------------\n'

        indexInput = IndexInput.objects.get(id=session_id)
        guyllyDB += str(indexInput.num_gully) + "\n"
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
                guyllyDB += str(getattr(g,GullyErosionInput_map[j])) + "\t"
            guyllyDB += "\n"    
        guyllyDB += '-----------------------\n'

        guyllyDB += str(indexInput.num_steambank) + "\n"
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
                guyllyDB += str(getattr(g,StreambankErosionInput_map[j])) + "\t"
            guyllyDB += "\n"    
        
        #WildLife.txt
        WildLife = ""
        keyMap = ['Goose','Deer','Beaver','Raccoons','Other']
        for key in keyMap:
            w = WildlifeDensityInCropLandInput.objects.get(session_id=session_id,Wildlife=key)
            WildLife += str('%.2f' % w.NumPerMileSquare) + "\n"

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

        #Feedlot.txt
        Feedlot = ""
        Animals = ['','Slaughter Steer','Young Beef','Dairy Cow','Young Dairy Stock','Swine','Feeder Pig','Sheep','Horse','Chicken','Turkey','Duck']
        for i in range(1,12):
            Animal = Animals[i]
            r = FeedlotAnimalInput.objects.get(session_id=session_id,Animal=Animal)
            Feedlot += '%.3f' % r.N + "\t"
            Feedlot += '%.3f' % r.P + "\t"
            Feedlot += '%.3f' % r.BOD + "\t"
            Feedlot += '%.3f' % r.COD + "\t"
            Feedlot += "\n"

        #pcp.txt
        #mainINP.txt
        #Septic.txt
        #LandRain_GW1.txt
        #BMPs.txt

        #URL_RUN_STEP_1 is from stepl_setting
        ret = requests.post(URL_RUN_STEP_1,data={
            "GullyDB.txt":guyllyDB,'WildLife.txt':WildLife，"Reference.txt" : Reference,
            })
        return ret.text



