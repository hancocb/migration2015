from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import IndexInput

class InputMainView(View):
    
    def post(self, request, *args, **kwargs):
    	#save to db(or session)
    	#<input type="hidden" name="ystimeldc" value="noldc">
    	#<input type="hidden" name="allPct" value="None">
    	# only the data that need to be edit would be written to template html
    	
    	#always use the session as context
        i = IndexInput(num_watershd=request.POST['numWSD'],
                        num_gully=request.POST['numGLY'],
                        num_steambank=request.POST['numSTR'])
        i.save()

        context = request.session
        context['rangeWSD'] = range( 1 , int( request.POST['numWSD'] ) + 1 )
        context['rangeGLY'] = range( 1 , int( request.POST['numGLY'] ) + 1 )
        context['rangeSTR'] = range( 1 , int( request.POST['numSTR'] ) + 1 )
        for i in range(2,10):
        	context['range' + str(i)] = range( 1, i + 1 )
        return render(request, 'inputMain.html', {'ctx':context, 'req' : request });


    def get(self, request):
    	raise Http404("GET of this page does not exist, you need POST")