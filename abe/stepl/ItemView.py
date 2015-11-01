from django.views.generic import View
from models import *
from django.shortcuts import render
from tools import list2dict,extract
from django.forms import modelform_factory
from django.http import JsonResponse

class ItemView(View):
    
    class_map = {
                    'CountyDataInput':(CountyDataInput,("id","session_id","state_name","name")),
                    'IndexInput':(IndexInput,("id","session_id")),
                    'SoilDataInput':(SoilDataInput,("id","session_id","watershd_id")),
                    'ReferenceRunoffInput':(ReferenceRunoffInput,("id","session_id","Landuse")),
                    'DetailedRunoffInput':(DetailedRunoffInput,("id","session_id","Urban")),
                    'NutrientRunoffInput':(NutrientRunoffInput,("id","session_id","Landuse")),
                    'NutrientGroundwaterRunoffInput':(NutrientGroundwaterRunoffInput,("id","session_id","Landuse")),
                    'LanduseDistributionInput':(LanduseDistributionInput,("id","session_id","watershd_id")),
                    'IrrigationInput':(IrrigationInput,("id","session_id","watershd_id")),
                    'SoilInfiltrationFractionInput':(SoilInfiltrationFractionInput,("id","session_id","HSG")),
                    'WildlifeDensityInCropLandInput':(WildlifeDensityInCropLandInput,("id","session_id","Wildlife")),
                    'AnimalWeightInput':(AnimalWeightInput,("id","session_id","Animal")),
                    'SepticSystemInput':(SepticSystemInput,("id","session_id","Title")),
                    'FeedlotAnimalInput':(FeedlotAnimalInput,("id","session_id","Animal")),
                    'SoilTextureInput':(SoilTextureInput,("id","session_id","Soil_Textural_Class")),
                    'LateralRecessionRateInput':(LateralRecessionRateInput,("id","session_id","Category","LRR")),
                    'GullyErosionInput':(GullyErosionInput,("id","session_id","Gully_id")),
                    'StreambankErosionInput':(StreambankErosionInput,("id","session_id","Streambank_id")),
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






