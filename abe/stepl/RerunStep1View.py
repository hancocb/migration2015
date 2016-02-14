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

class RerunStep1View(View):
    
    def get(self, request, *args, **kwargs):

        #all saved to session
        context = request.session
        session_id = request.GET['session_id']
        
        context['IndexInput'] = {}
        context['IndexInput']['id'] = session_id 

        indexInput = IndexInput.objects.get(id=session_id)

        context['rangeWSD'] = range( 1 , int( indexInput.num_watershd ) + 1 )
        context['rangeGLY'] = range( 1 , int( indexInput.num_gully ) + 1 )
        context['rangeSTR'] = range( 1 , int( indexInput.num_steambank ) + 1 )


        for i in range(2,10):
            context['range' + str(i)] = range( 1, i + 1 )

        #process through STPEL api to run fortran
        from_id = URL_RUN_FROM_ID + str(request.GET['session_id'])
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

    def post(self, request):
        raise Http404("GET of this page does not exist, you need get")

    