from django.views.generic import View
from models import *
from django.shortcuts import render
from tools import list2dict,extract
from django.forms import modelform_factory
from django.http import JsonResponse

class ItemView(View):
    
    class_map = {
                    'CountyDataInput':(CountyDataInput,("id","session_id","state_name","name")),
                    'IndexInput':IndexInput,
                    'SoilDataInput':SoilDataInput,
                    'ReferenceRunoffInput':ReferenceRunoffInput,
                    'DetailedRunoffInput':DetailedRunoffInput,
                    'NutrientRunoffInput':NutrientRunoffInput,
                    'NutrientGroundwaterRunoffInput':NutrientGroundwaterRunoffInput,
                    'LanduseDistributionInput':LanduseDistributionInput,
                    'IrrigationInput':IrrigationInput,
                    'SoilInfiltrationFractionInput':SoilInfiltrationFractionInput,
                    'WildlifeDensityInCropLandInput':WildlifeDensityInCropLandInput,
                    'AnimalWeightInput':AnimalWeightInput,
                    'SepticSystemInput':SepticSystemInput,
                    'FeedlotAnimalInput':FeedlotAnimalInput,
                    'SoilTextureInput':SoilTextureInput,
                    'LateralRecessionRateInput':LateralRecessionRateInput,
                    'GullyErosionInput':GullyErosionInput,
                    'StreambankErosionInput':StreambankErosionInput,
                }

    def get(self, request, modelName, id):
        context = request.session
        session_id = context['IndexInput']['id']

        _model = self.class_map[modelName][0]
        item = _model.objects.get(session_id=session_id,id=id)
        
        if 's' in request.GET:
            exclude = self.class_map[modelName][1]
            _form = modelform_factory(_model,exclude=exclude)
            form = _form(instance=item)
            return render(request, 'updateItem.html', { 'modelName':modelName, 'form':form, 'status': 0 })
        else:    
            return JsonResponse(extract(item))

    def post(self,request,modelName,id):
        context = request.session
        session_id = context['IndexInput']['id']

        _model = self.class_map[modelName][0]
        exclude = self.class_map[modelName][1]
        _form = modelform_factory(_model,exclude=exclude)
        item = _model.objects.get(session_id=session_id,id=id)
        form = _form(request.POST, instance=item)
        status = form.save()
        return render(request, 'updateItem.html', { 'modelName':modelName, 'form':form, 'status':status })






