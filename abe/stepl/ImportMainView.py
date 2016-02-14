from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt   


class ImportMainView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ImportMainView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        #all saved to session
        context = request.session

        #from login page, check username,psw then use the data from session
        if 'username' in request.POST :
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                #psw/username are correct
                context['hasLogin'] = True
                context['username'] = username
                return self.renderFromPost(context,request)    
            else: #error psw and username, goback to login page
                context['nextAction'] = '/stepl/importMain'
                return render(request, 'mapstepl/login.html', { 'ctx':context, 'req' : request })

        #from lthia and has logined, use the post data     
        elif 'hasLogin' in context and context['hasLogin'] :
            context['fromLthia'] = self.processPost(request.POST)
            return self.renderFromPost(context,request)
        #from lthia but not logined, save data to session and goto login page    
        else:
            context['fromLthia'] = self.processPost(request.POST)
            context['nextAction'] = '/stepl/importMain'
            return render(request, 'mapstepl/login.html', { 'ctx':context, 'req' : request })

    def processPost(self,postData):
        ret = {}
        ret['numWSD'] = int(postData['numWSD'])
        ret['numGLY'] = int(postData['numGLY'])
        ret['numSTR'] = int(postData['numSTR'])

        lanuserArr = postData['land_list'].split(" ")
        ret['landUse'] = {}
        ret['landUse']['1'] = {}
        ret['landUse']['2'] = {}
        ret['landUse']['3'] = {}
        ret['landUse']['4'] = {}

        ret['landUse']['1']['HSG'] = 'A'
        ret['landUse']['2']['HSG'] = 'B'
        ret['landUse']['3']['HSG'] = 'C'
        ret['landUse']['4']['HSG'] = 'D'

        for i in range(1,5):
            for k in range(1,7):
                ret['landUse'][str(i)][str(k)] = float(lanuserArr[ (i-1)*8+k-1 ] )
        
        #TODO, need to get it from lthia!!!!
        ret['hucid'] = "123"
        return ret

    def renderFromPost(self,context,request):        
    	#save the last step of data,create new session
        i = IndexInput(num_watershd= context['fromLthia']['numWSD'],
                        num_gully= context['fromLthia']['numGLY'],
                        num_steambank= context['fromLthia']['numSTR'])
        i.save()

        #save the session under this user
        userSession = UserSession(username=context['username'],session_id=i.id,hucid=context['fromLthia']['hucid'])
        userSession.save()
        
        context['IndexInput'] = {}
        context['IndexInput']['id'] = i.id

        context['rangeWSD'] = range( 1 , int( context['fromLthia']['numWSD'] ) + 1 )
        context['rangeGLY'] = range( 1 , int( context['fromLthia']['numGLY'] ) + 1 )
        context['rangeSTR'] = range( 1 , int( context['fromLthia']['numSTR'] ) + 1 )

        for i in range(2,10):
        	context['range' + str(i)] = range( 1, i + 1 )

        #prepare data    
        self.prepareOptMainView(request)
        self.prepareOthers(request)

        return render(request, 'importMain.html', { 'ctx':context, 'req' : request })

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


