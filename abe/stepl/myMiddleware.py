from models import *

class LocaleMiddleware(object):

    def process_request(self, request):
        context = request.session

        #making choices for watershed dynamically
        try:
            GullyErosionInput.models_choices_tuple = []
            for i in context['rangeWSD']:
               GullyErosionInput.models_choices_tuple.append(  (i,'W'+str(i) ) )
        except:
            pass      
        print request

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin']  = "*" 
        response['X-Frame-Options']  = 'ALLOWALL'
        return response