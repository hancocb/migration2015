from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

class CLIGENMapView(View):

    def get(self, request, *args, **kwargs):
        context = request.session
        return render(request, 'CLIGENMap.html', {'ctx':context, 'req' : request });
