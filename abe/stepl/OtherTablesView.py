from django.views.generic import View
from models import *
from django.shortcuts import render
from tools import list2dict
from django.http import Http404

class OtherTablesView(View):
    
    def get(self, request):
        template = request.GET['t']
        context = request.session
        session_id = context['IndexInput']['id']
        if template == 'soilInfiltrationRatio':
            context['SoilInfiltrationFractionInput'] = list2dict(SoilInfiltrationFractionInput.objects.filter(session_id=session_id).values())
        elif template == 'wildlife':
            context['WildlifeDensityInCropLandInput'] = list2dict(WildlifeDensityInCropLandInput.objects.filter(session_id=session_id).values())
        elif template == 'animalWeight':
            context['AnimalWeightInput'] = list2dict(AnimalWeightInput.objects.filter(session_id=session_id).values())
        elif template == 'septic':
            context['SepticSystemInput'] = list2dict(SepticSystemInput.objects.filter(session_id=session_id).values())
        elif template == 'freelot':
            context['FreelotAnimalInput'] = list2dict(FreelotAnimalInput.objects.filter(session_id=session_id).values())
        elif template == 'gullyDB':
            context['SoilTextureInput'] = list2dict(SoilTextureInput.objects.filter(session_id=session_id).values())
            context['LateralRecessionRateInput'] = list2dict(LateralRecessionRateInput.objects.filter(session_id=session_id).values())
        elif template == 'gullyNstreambankErosion':
            context['GullyErosionInput'] = list2dict(GullyErosionInput.objects.filter(session_id=session_id).values())
            context['StreambankErosionInput'] = list2dict(StreambankErosionInput.objects.filter(session_id=session_id).values())
            #change choices for model according to the watershd
        elif template == 'urbanBMP' or template == 'urbanBMPClick':
            pass    
        else:
            raise Http404("no such template")
   
        return render(request, template+'.html', { 'ctx':context, 'req' : request })


