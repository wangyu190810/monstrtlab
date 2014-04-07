#coding:utf-8
from form import RegisterForm,LoginForm,ChangepwdForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def register(request):
    error =[]
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            email=data['email']
            password=data['password']
            password2=data['password2']
            if not User.objects.all().filter(username=username):
                if form.pwd_validate(password,password2):
                    user=User.objects.create_user(username,email,password)
                    user.save()
                    login_validate(request,username,password)
                    return render_to_response('index.html',{'user':username},context_instance=RequestContext(request));
                else:
                    error.append('Please input the same password ')
            else:
                error.append('The username is existed,please type anthor  usrename')
    else:
        form=RegisterForm()
    return render_to_response('register.html',{'form':form,'error':error})
def login_validate(request,username,password):
    rtvalue=False
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            return True
    return rtvalue




# Create your views here.
