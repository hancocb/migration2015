from django.views.generic import View
from models import SoilData,SoilDataInput
from django.shortcuts import render


class OptMainView(View):

    def get(self, request):
        context = request.session
        context['soilInput'] = {}

        for i in context['rangeWSD']:
            soilInput = SoilDataInput.objects.get(session_id=context['IndexInput']['id'],watershd_id = i)    
            context['soilInput'][i] = soilInput.id
        return render(request, 'optMain.html', { 'ctx':context, 'req' : request })


