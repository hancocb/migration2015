from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from stepl.tools import list2dict
from models import *
from django.contrib.auth import authenticate, logout


class LogoutView(View):
    #GET: check session, fail then goto login
    def get(self, request):
        #all saved to session
        context = request.session
        context['hasLogin'] = False
        logout(request)
        context['nextAction'] = '/stepl/userSession'
        return render(request, 'mapstepl/login.html', { 'ctx':context, 'req' : request })
    def post(self,request):
        context = request.session
        context['hasLogin'] = False
        logout(request)
        return JsonResponse({'succ':True})