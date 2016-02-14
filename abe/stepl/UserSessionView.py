from django.views.generic import View
from models import *
from django.shortcuts import render
from tools import list2dictWthCTime,extract
from django.forms import modelform_factory
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


class UserSessionView(View):
    
    def get(self, request ):
        context = request.session
        if 'hasLogin' in context and context['hasLogin'] :
            sessions = UserSession.objects.filter(username=context['username']).values()
            return render(request, 'mapstepl/userSession.html', { 'ctx':sessions, 'req' : request })

        #from lthia but not logined, login page    
        else:
            context['nextAction'] = '/stepl/userSession'
            return render(request, 'mapstepl/login.html', { 'ctx':context, 'req' : request })
                

    def post(self, request ):
        #all saved to session
        context = request.session

        #from login page, check username,psw then display
        if 'username' in request.POST :
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                #psw/username are correct
                context['hasLogin'] = True
                context['username'] = username
                sessions = UserSession.objects.filter(username=context['username']).values()
                return render(request, 'mapstepl/userSession.html', { 'ctx':sessions, 'req' : request })
            else: #error psw and username, goback to login page
                context['nextAction'] = '/stepl/userSession'
                return render(request, 'mapstepl/login.html', { 'ctx':context, 'req' : request })

        #from lthia and has logined, display
        elif 'hasLogin' in context and context['hasLogin'] :
            sessions = UserSession.objects.filter(username=context['username']).values()
            return render(request, 'mapstepl/userSession.html', { 'ctx':sessions, 'req' : request })

        #from lthia but not logined, login page    
        else:
            context['nextAction'] = '/stepl/userSession'
            return render(request, 'mapstepl/login.html', { 'ctx':context, 'req' : request })
                


