from stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import *
from templatetags.simple_tags import twonum
from tools import extract
from utils import requests
import json
from RunStep1 import *

class RunStep1View(View):
    
    def post(self, request, *args, **kwargs):

        #all saved to session
        context = request.session
        session_id=context['IndexInput']['id']
        #process inputs from bmpMain

        #process landtype_id: 1~5 : Cropland, pastland, forest,user defined,feedlot
        for landtype_id in range(1,6):
            for watershd_id in context['rangeWSD']:
                if not BMPInput.objects.filter(session_id=session_id, landtype_id=landtype_id ,
                    watershd_id=watershd_id).exists():
                    bmpInput = BMPInput(
                        session_id=session_id, 
                        landtype_id=landtype_id,
                        watershd_id=watershd_id
                        )
                else:
                    bmpInput = BMPInput.objects.get(session_id=session_id, landtype_id=landtype_id, 
                        watershd_id=watershd_id)
                bmpInput.BMP = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"5"]
                bmpInput.PercentApplied=request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"6"]
                bmpInput.N   = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"1"]
                bmpInput.P   = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"2"]
                bmpInput.BOD = request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"3"]
                bmpInput.Sediment=request.POST['BMP_'+str(landtype_id)+"_"+twonum(watershd_id)+"4"]
                bmpInput.save()

        #UrbnConc
        for i in range(1,5):
            for j in range(1,10):
                key = "UrbnConc_"+str(i)+str(j)
                if not UrbanBmpInput.objects.filter(session_id=session_id, key=key).exists():
                    urbanBmpInput = UrbanBmpInput(
                        session_id=session_id, 
                        key=key
                        )
                else:
                    urbanBmpInput = UrbanBmpInput.objects.get(session_id=session_id, key=key)
                urbanBmpInput.value = request.POST[key]
                urbanBmpInput.save()

        #UrbanBMP_
        for k in context['range5']:
            for i in context['rangeWSD']:
                for j in context['range9']: 
                    key = 'UrbanBMP_'+str(k)+'_'+twonum(i)+str(j) 
                    if not UrbanBmpInput.objects.filter(session_id=session_id, key=key).exists():
                        urbanBmpInput = UrbanBmpInput(
                            session_id=session_id, 
                            key=key
                            )
                    else:
                        urbanBmpInput = UrbanBmpInput.objects.get(session_id=session_id, key=key)
                    urbanBmpInput.value = request.POST[key]
                    urbanBmpInput.save()

        #process through STPEL api to run fortran
        from_id = URL_RUN_FROM_ID + str(session_id)
        run1_url = FORTRAN_SERVER + URL_RUN_STEP_1
        text = runStep1(context,from_id,run1_url)
        print text

        #parse text
        ret = json.loads(text);
        clmArr = [0,1,3,4,5,7,8,9,11,12,13,15,16]
        img_prefix = FORTRAN_SERVER + "tmp/" + from_id + "/" 

        return render(request, 'runStep1.html', { 
            'ctx':context, 'req' : request, 'run1ret':ret['run1ret'][1:], 
            'img_prefix' : img_prefix, 'clmArr':clmArr
            })

    def get(self, request):
        raise Http404("GET of this page does not exist, you need POST")

    