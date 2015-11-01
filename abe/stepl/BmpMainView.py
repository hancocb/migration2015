from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from templatetags.simple_tags import twonum
from tools import extract,list2dictWthKey

class BmpMainView(View):
    
    def post(self, request, *args, **kwargs):

        #all saved to session
        context = request.session

        #process inputs from inputMain

        #process gwOpt and swsOpt
        indexInput = IndexInput.objects.get(id=context['IndexInput']['id'])
        if request.POST['gwOpt']!='on' or request.POST['swsOpt']!='on':
            if request.POST['gwOpt']!='on':
                indexInput.gwOpt=False
            if request.POST['swsOpt']!='on':
                indexInput.swsOpt=False
            indexInput.save()
        
        #process WatershedLandUse
        context['WatershedLandUse'] = {}
        for watershd_id in context['rangeWSD'] :
            if not WatershedLandUse.objects.filter(session_id=indexInput.id, watershd_id=watershd_id).exists():
                watershedLandUse = WatershedLandUse(
                    session_id=indexInput.id, 
                    watershd_id=watershd_id
                    )
            else:
                watershedLandUse = WatershedLandUse.objects.get(session_id=indexInput.id, watershd_id=watershd_id)
            watershedLandUse.HSG = request.POST['HSG_' + twonum(watershd_id)]
            watershedLandUse.FeedlotPercentPaved = request.POST['PctFeedlot_' + twonum(watershd_id)]
            watershedLandUse.Total = request.POST['TAreaWSD_' + twonum(watershd_id)]
            for i in range(1,7):
                setattr( watershedLandUse,WatershedLandUse_index_map[i],request.POST['LuseAreaWSD_'+str(i)+twonum(watershd_id)] )   
            watershedLandUse.save()
            #prepare data for rendering template
            context['WatershedLandUse'][watershd_id] = extract(watershedLandUse)

        #process AgriAnimal
        for watershd_id in context['rangeWSD'] :
            if not AgriAnimal.objects.filter(session_id=indexInput.id, watershd_id=watershd_id).exists():
                agriAnimal = AgriAnimal(
                    session_id=indexInput.id, 
                    watershd_id=watershd_id
                    )
            else:
                agriAnimal = AgriAnimal.objects.get(session_id=indexInput.id, watershd_id=watershd_id)
            agriAnimal.numMonthsManureApplied = request.POST['NumMonManure_' + twonum(watershd_id)]
            for i in range(1,9):
                setattr( agriAnimal,AgriAnimal_index_map[i],request.POST['Animals_'+str(i)+twonum(watershd_id)] )   
            agriAnimal.save()

        #process SepticNillegal
        for watershd_id in context['rangeWSD'] :
            if not SepticNillegal.objects.filter(session_id=indexInput.id, watershd_id=watershd_id).exists():
                septicNillegal = SepticNillegal(
                    session_id=indexInput.id, 
                    watershd_id=watershd_id
                    )
            else:
                septicNillegal = SepticNillegal.objects.get(session_id=indexInput.id, watershd_id=watershd_id)
            septicNillegal.numSepticSystems = request.POST['NumSpSys_' + twonum(watershd_id)]
            septicNillegal.PopulationPerSeptic = request.POST['PpSpSys_' + twonum(watershd_id)]
            septicNillegal.SepticFailureRate_Percent = request.POST['SpFailRate_' + twonum(watershd_id)]
            septicNillegal.Wastewater_Direct_Discharge_numPeople = request.POST['NumPpDrtDc_' + twonum(watershd_id)]
            septicNillegal.Direct_Discharge_Reduction_Percent = request.POST['RdcDrtDc_' + twonum(watershd_id)]
            septicNillegal.save()

        #load LanduseDistribution    
        context['LanduseDistributionInput'] = list2dictWthKey('watershd_id',LanduseDistributionInput.objects.filter(session_id=indexInput.id).values())    

        return render(request, 'bmpMain.html', { 'ctx':context, 'req' : request })

    def get(self, request):
    	raise Http404("GET of this page does not exist, you need POST")



