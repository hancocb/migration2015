from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from django.contrib.auth import authenticate, login

class InputMainView(View):
    
    def post(self, request, *args, **kwargs):

        #login user for editing
        username = "guest"
        password = "guest"
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

        #all saved to session
        context = request.session

    	#save the last step of data
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
        pass

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
        all_eles = UrbanReferenceRunoff.objects.all()
        for ele in all_eles:
            if not UrbanReferenceRunoffInput.objects.filter(
                session_id=context['IndexInput']['id'],Landuse=ele.Landuse).exists():
                inp = UrbanReferenceRunoffInput(
                        SHG_A = ele.SHG_A, 
                        SHG_B = ele.SHG_B, 
                        SHG_C = ele.SHG_C, 
                        SHG_D = ele.SHG_D,
                        Landuse = ele.Landuse,
                        session_id = context['IndexInput']['id'] ,
                    )
                inp.save()
        #6a. Detailed urban reference runoff curve number
        all_eles = DetailedRunoff.objects.all()
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
        all_eles = NutrientRunoff.objects.all()
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
        all_eles = NutrientGroundwaterRunoff.objects.all()
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


