#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from django.template.context import RequestContext 
from login.models import *
from login.forms.AccountForm import LoginForm


def Login(request):
    data = {'LoginStatus':''}
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        password = postData.get('password')
        print username,password
        
        if username and password:
            result = UserInfo.objects.filter(UserName=username,Password=password).count()
            if result == 1:
                return redirect('/admin/index')
        data['LoginStatus'] = '用户名或密码错误.'
    return render_to_response('Account/Login.html',data,context_instance=RequestContext(request))

def LoginByForm(request):
    if request.method == 'POST':
        data = request.POST
        loginForm = LoginForm(data)
        loginForm.as_table
        if loginForm.is_valid():
            da = loginForm.cleaned_data
            return HttpResponse('OK')
        else:
            return render_to_response('Account/LoginForm.html',{'model':loginForm},context_instance=RequestContext(request))
    loginForm = LoginForm()
    return render_to_response('Account/LoginForm.html',{'model':loginForm},context_instance=RequestContext(request))
        
def Logout(request):
    pass

def Register(request):
    pass

    
    
    
    
    