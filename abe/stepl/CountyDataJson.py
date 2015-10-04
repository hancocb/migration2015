from django.http import JsonResponse
from django.views.generic import View
from models import CountyData
from models import CountyDataInput
from django.core import serializers

class CountyDataJson(View):

	def get(self, request):
		ele = CountyData.objects.get(state_name=request.GET['State'],name=request.GET['County'])

		if not CountyDataInput.objects.filter(session_id=request.session['IndexInput']['id']).exists():
			cntInput = CountyDataInput(
				state_name = ele.state_name,
				name  = ele.name,
				rmean = ele.rmean,
				kmean = ele.kmean,
				lsavg = ele.lsavg,
				cavg = ele.cavg,
				pavg = ele.pavg,
				session_id = request.session['IndexInput']['id']
				)
			cntInput.save()
		else:
			cntInput = CountyDataInput.objects.get(session_id=request.session['IndexInput']['id'])


		#fields = CountyData._meta.get_all_field_names()
		#for f in fields:
		#	data[f] = getattr(ele,f)

		#total = Rval[0] + Rval[1] + USLE[0] + USLE[1] + USLE[2] + USLE[3] + USLE[4]
		total = ele.rainfall_inches + ele.raindays + ele.rmean + ele.kmean + ele.lsavg +ele.cavg +ele.pavg
		data = {}
		data['total'] = total
		data['CountyDataInput_id'] = cntInput.id
		if total != 0 :
			data['ret'] = [ 
				ele.rmean , ele.kmean, ele.lsavg, #0,1,2
				max(ele.cavg,0.2),
				ele.pavg, #4
				ele.rmean , ele.kmean, ele.lsavg,#0,1,2
				0.04,
				ele.pavg, #4
				ele.rmean , ele.kmean, ele.lsavg,#0,1,2
				0.03,
				ele.pavg, #4
				ele.rmean , ele.kmean, ele.lsavg,#0,1,2
				ele.cavg, #3
				ele.pavg, #4
				]
		else :
			data['ret'] = [ 
				0,0,0,
				max(ele.cavg,0.2),
				0,0,0,0,
				0.04,
				0,0,0,0,
				0.03,
				0,0,0,0,0,0,
				]
		return JsonResponse(data)


