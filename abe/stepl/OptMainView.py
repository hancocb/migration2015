from django.views.generic import View
from models import *
from django.shortcuts import render
from tools import list2dict

class OptMainView(View):
    
    def get(self, request):
        context = request.session
        session_id = context['IndexInput']['id']
        #5
        context['SoilDataInput'] = list2dict(SoilDataInput.objects.filter(session_id=session_id).values())
        #6
        context['ReferenceRunoffInput'] = list2dict(ReferenceRunoffInput.objects.filter(session_id=session_id).values())
        #6.a
        context['DetailedRunoffInput'] = list2dict(DetailedRunoffInput.objects.filter(session_id=session_id).values())
        #7
        context['NutrientRunoffInput'] = list2dict(NutrientRunoffInput.objects.filter(session_id=session_id).values())
        #7.a
        context['NutrientGroundwaterRunoffInput'] = list2dict(NutrientGroundwaterRunoffInput.objects.filter(session_id=session_id).values())
        #8
        context['LanduseDistributionInput'] = list2dict(LanduseDistributionInput.objects.filter(session_id=session_id).values())
        #9
        context['IrrigationInput'] = list2dict(IrrigationInput.objects.filter(session_id=session_id).values())
            
        return render(request, 'optMain.html', { 'ctx':context, 'req' : request })


