# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf

from app.user_life_logic import User_reg_log

def login(request):
    user = User_reg_log()
    return user.login_in_system(request)


def logout(request):
     auth.logout(request)
     return redirect('/')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {})
    return render(request, 'index.html', {'user': None})

def registry(request):
    if not request.user.is_authenticated:
        user = User_reg_log()
        result, err = user.registry_user(request)
        email = request.POST.get('email_reg', '')
        if result:
            pass1 = request.POST.get('pass1_reg', '')
            user = auth.authenticate(username=email, password=pass1)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'index.html', {'user': None, 'error': err, 'email': email})
    return redirect('/')
