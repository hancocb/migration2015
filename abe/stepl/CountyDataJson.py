from django.http import JsonResponse
from django.views.generic import View
from models import CountyData
from django.core import serializers

class CountyDataJson(View):

	def get(self, request):
		ele = CountyData.objects.get(state_name=request.GET['State'],name=request.GET['County'])
		fields = CountyData._meta.get_all_field_names()
		data = {}
		#for f in fields:
		#	data[f] = getattr(ele,f)

		#total = Rval[0] + Rval[1] + USLE[0] + USLE[1] + USLE[2] + USLE[3] + USLE[4]
		total = ele.rainfall_inches + ele.raindays + ele.rmean + ele.kmean + ele.lsavg +ele.cavg +ele.pavg
		data['total'] = total
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


