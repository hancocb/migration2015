from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import IndexInput,SoilDataInput,SoilData,UrbanReferenceRunoff,UrbanReferenceRunoffInput
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
            
        return render(request, 'inputMain.html', { 'ctx':context, 'req' : request })

    def get(self, request):
    	raise Http404("GET of this page does not exist, you need POST")

    def prepareOptMainView(self,request):
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
        '''
            "Industrial",
            "Institutional",
            "Transportation",
            "Multi-Family",
            "Single-Family",
            "Urban-Cultivated",
            "Vacant-Developed",
            "Open Space",
        '''
        urban_types = [
            "Commercial",
            ]
        for uburn in urban_types:
            if not UrbanReferenceRunoffInput.objects.filter(session_id=context['IndexInput']['id'],Urban=uburn).exists():
                ele = UrbanReferenceRunoff.objects.get(Urban=uburn)
                soilInput = UrbanReferenceRunoffInput(
                        SHG_A = ele.SHG_A, 
                        SHG_B = ele.SHG_B, 
                        SHG_C = ele.SHG_C, 
                        SHG_D = ele.SHG_D,
                        Urban = ele.Urban,
                        session_id = context['IndexInput']['id'] ,
                    )
                soilInput.save()


