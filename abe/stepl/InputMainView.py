from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from django.contrib.auth import authenticate, login

class InputMainView(View):
    
    def post(self, request, *args, **kwargs):

        #all saved to session
        context = request.session

    	#save the last step of data,create new session
        i = IndexInput(num_watershd=request.POST['numWSD'],
                        num_gully=request.POST['numGLY'],
                        num_steambank=request.POST['numSTR'])
        i.save()
        context['IndexInput'] = {}
        context['IndexInput']['id'] = i.id

        context['rangeWSD'] = range( 1 , int( request.POST['numWSD'] ) + 1 )
        context['rangeGLY'] = range( 1 , int( request.POST['numGLY'] ) + 1 )
        context['rangeSTR'] = range( 1 , int( request.POST['numSTR'] ) + 1 )

        for i in range(2,10):
        	context['range' + str(i)] = range( 1, i + 1 )

        #prepare data    
        self.prepareOptMainView(request)
        self.prepareOthers(request)

        return render(request, 'inputMain.html', { 'ctx':context, 'req' : request })

    def get(self, request):
    	raise Http404("GET of this page does not exist, you need POST")
    #gwInfRatio,WildLife,Reference,Septic,Feedlot,GullyDB,Gully&Steambank Erosion    
    def prepareOthers(self,request):
        abstract_models = [
            SoilInfiltrationFractionAbstract,
            WildlifeDensityInCropLandAbstract,
            AnimalWeightAbstract,
            SepticSystemAbstract,
            FeedlotAnimalAbstract,
            SoilTextureAbstract,
            LateralRecessionRateAbstract,
        ]
        sample_models = [
            SoilInfiltrationFraction,
            WildlifeDensityInCropLand,
            AnimalWeight,
            SepticSystem,
            FeedlotAnimal,
            SoilTexture,
            LateralRecessionRate,
        ]
        input_models = [
            SoilInfiltrationFractionInput,
            WildlifeDensityInCropLandInput,
            AnimalWeightInput,
            SepticSystemInput,
            FeedlotAnimalInput,
            SoilTextureInput,
            LateralRecessionRateInput,
        ]

        context = request.session
        for i in range(0,7):
            all_eles = sample_models[i].objects.filter(Standard = INPUT_STANDARD).order_by('id')
            for ele in all_eles:
                inp = input_models[i](
                            session_id = context['IndexInput']['id'] ,
                        )
                for fd in abstract_models[i]._meta.get_all_field_names():
                    setattr(inp,fd,getattr(ele,fd))
                inp.save()

        ele = GullyErosion.objects.get(Standard = INPUT_STANDARD)
        for i in context['rangeGLY']:
            inp = GullyErosionInput(
                    session_id = context['IndexInput']['id'] ,
                    watershd_id = 0,
                    Gully_id = i,
                )
            for fd in GullyErosionAbstract._meta.get_all_field_names():
                setattr(inp,fd,getattr(ele,fd))
            inp.save()

        ele = StreambankErosion.objects.get(Standard = INPUT_STANDARD)
        for i in context['rangeSTR']:
            inp = StreambankErosionInput(
                    session_id = context['IndexInput']['id'] ,
                    watershd_id = 0,
                    Streambank_id = i,
                )
            for fd in StreambankErosionAbstract._meta.get_all_field_names():
                setattr(inp,fd,getattr(ele,fd))
            inp.save()

    #as a better way , can see prepareOthers() which use class array, 
    #we can refactory it when we are going to extend the Standard for more options
    def prepareOptMainView(self,request):
        context = request.session
        #5. soil data
        ele = SoilData.objects.get(Standard = INPUT_STANDARD)
        for i in context['rangeWSD']:
            if not SoilDataInput.objects.filter(session_id=context['IndexInput']['id'],watershd_id = i).exists():
                soilInput = SoilDataInput(
                        Soil_N_Conc =  ele.Soil_N_Conc,
                        Soil_P_Conc =  ele.Soil_P_Conc,
                        Soil_BOD_Conc =  ele.Soil_BOD_Conc,
                        session_id = context['IndexInput']['id'] ,
                        watershd_id = i
                    )
                soilInput.save()

        #6.Reference runoff curve number
        all_eles = ReferenceRunoff.objects.filter(Standard = INPUT_STANDARD).order_by('id')
        for ele in all_eles:
            if not ReferenceRunoffInput.objects.filter(
                session_id=context['IndexInput']['id'],Landuse=ele.Landuse).exists():
                inp = ReferenceRunoffInput(
                        SHG_A = ele.SHG_A, 
                        SHG_B = ele.SHG_B, 
                        SHG_C = ele.SHG_C, 
                        SHG_D = ele.SHG_D,
                        Landuse = ele.Landuse,
                        session_id = context['IndexInput']['id'] ,
                    )
                inp.save()
        #6a. Detailed urban reference runoff curve number
        all_eles = DetailedRunoff.objects.filter(Standard = INPUT_STANDARD).order_by('id')
        for ele in all_eles:
            if not DetailedRunoffInput.objects.filter(
                session_id=context['IndexInput']['id'],Urban=ele.Urban).exists():
                inp = DetailedRunoffInput(
                        SHG_A = ele.SHG_A, 
                        SHG_B = ele.SHG_B, 
                        SHG_C = ele.SHG_C, 
                        SHG_D = ele.SHG_D,
                        Urban = ele.Urban,
                        session_id = context['IndexInput']['id'] ,
                    )
                inp.save()

        #7.Nutrient concentration in runoff (mg/l)
        all_eles = NutrientRunoff.objects.filter(Standard = INPUT_STANDARD).order_by('id')
        for ele in all_eles:
            if not NutrientRunoffInput.objects.filter(
                session_id=context['IndexInput']['id'],Landuse=ele.Landuse).exists():
                inp = NutrientRunoffInput(
                        N = ele.N, 
                        P = ele.P, 
                        BOD = ele.BOD, 
                        Landuse = ele.Landuse,
                        session_id = context['IndexInput']['id'] ,
                    )
                inp.save()
        #7a Nutrient concentration in shallow groundwater (mg/l)
        all_eles = NutrientGroundwaterRunoff.objects.filter(Standard = INPUT_STANDARD).order_by('id')
        for ele in all_eles:
            if not NutrientGroundwaterRunoffInput.objects.filter(
                session_id=context['IndexInput']['id'],Landuse=ele.Landuse).exists():
                inp = NutrientGroundwaterRunoffInput(
                        N = ele.N, 
                        P = ele.P, 
                        BOD = ele.BOD, 
                        Landuse = ele.Landuse,
                        session_id = context['IndexInput']['id'] ,
                    )
                inp.save()
        #8. Input or modify urban land use distribution
        ele = LanduseDistribution.objects.get(Standard = INPUT_STANDARD)
        for i in context['rangeWSD']:
            if not LanduseDistributionInput.objects.filter(session_id=context['IndexInput']['id'],watershd_id = i).exists():
                inp = LanduseDistributionInput(
                        session_id = context['IndexInput']['id'] ,
                        watershd_id = i
                    )
                for fd in LanduseDistributionAbstract._meta.get_all_field_names():
                    setattr(inp,fd,getattr(ele,fd))
                inp.save()
        #9. Input irrigation area (ac) and irrigation amount (in)
        ele = Irrigation.objects.get(Standard = INPUT_STANDARD)
        for i in context['rangeWSD']:
            if not IrrigationInput.objects.filter(session_id=context['IndexInput']['id'],watershd_id = i).exists():
                inp = IrrigationInput(
                        session_id = context['IndexInput']['id'] ,
                        watershd_id = i
                    )
                for fd in IrrigationAbstract._meta.get_all_field_names():
                    setattr(inp,fd,getattr(ele,fd))
                inp.save()
        #end for optMain


