from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import IndexInput,SoilDataInput,SoilData
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
        prepareOptMainView()
            
        return render(request, 'inputMain.html', { 'ctx':context, 'req' : request })

    def get(self, request):
    	raise Http404("GET of this page does not exist, you need POST")

    def prepareOptMainView():
        context = request.session
        #1. soil data
        ele = SoilData.objects.get(SHG='A')
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
        #Detailed urban reference runoff curve number
        urban_types = [
            "Commercial",
            "Industrial",
            "Institutional",
            "Transportation",
            "Multi-Family",
            "Single-Family",
            "Urban-Cultivated",
            "Vacant-Developed",
            "Open Space",
            ]
        for uburn in urban_types:
            if not UrbanReferenceRunoffInput.objects.filter(session_id=context['IndexInput']['id'],watershd_id = i).exists():

                soilInput = UrbanReferenceRunoffInput(
                        Soil_N_Conc =  ele.Soil_N_Conc,
                        Soil_P_Conc =  ele.Soil_P_Conc,
                        Soil_BOD_Conc =  ele.Soil_BOD_Conc,
                        session_id = context['IndexInput']['id'] ,
                        watershd_id = i
                    )
                soilInput.save()


