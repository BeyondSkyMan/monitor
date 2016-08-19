#!/usr/bin/env python
#coding:utf-8


from django import forms
#from django import forms.ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=2)
    password = forms.CharField(max_length=2,widget=forms.PasswordInput())
    email = forms.EmailField(max_length=20)
    