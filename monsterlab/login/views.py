#coding:utf-8
from form import RegisterForm,LoginForm,ChangepwdForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#找回密码
from login.models import FindPassword
from utils.utils import *
from threading import Thread
from datetime import date
import sys
import random
import string
from time import strftime

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
def login(request):
    error=[]
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            password=data['password']
            if login_validate(request,username,password):
#               return render_to_response('index.html',{'user':username})
                return render_to_response('index.html',{'user':username},context_instance=RequestContext(request));
            else:
                error.append('please in put eorrect password')
        else:
            error.append('Please input both username and password')
    else:
        form=LoginForm()
    return render_to_response('login.html',{'error':error,'form':form})
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('regist')

def forget_password(request):
    emial=request.POST['email']
    user=User.objects.get(email=email)
    if user:
        #生成字符串
        activation_key=random_string(random,randint(10,20));
        findPasses=FindPassword.objects.filter(username=user.username)
        if findPasses:
            findPass=findPasses[0]
            findPass.activetion_key=activetion_key
        else:
            findPass=FindPass(username=user.username,activetion_key=activetion_key)
        findPass.save()
        th=Thread(target=send_html_mail,
                args=('重置密码！3天有效',
                    'click hte url
                    http://127.0.0.1:8000/resetpassword'+activetion_key,
                    [email]))
                th.start()

                return render_to_response('forgetpassword.html')
    else:
        return render_to_response('404.html')
def random_string(num):
    password=''
    seed=string.letters+string.digits
    for i in  range(num):
        password +=seed[random.randrange(1,len(seed)]
    return password

def begin_reset_password(request,activetion_key):
    findPasses=FindPassword.objects.filter(activetion_key=activetion_key)
    if findPasses:
        findPasses=findPasses[0]
        if int(data.today().strftime('%Y%m%d'))-int(findPass.date.strftime('%Y%m%d'))<3:
            
            user=User.objects.get(username=findPass.username)
            request.session['findpasser']=user

            return render_to_response('begin_reset_password.html',{'user':user})
    return render_to_response('404,html')
def reset_password(request):
    password=request.POST['password']
    user=request.session['findpasser']
    if user:
        user.set_password(password)
        user.save
        
        FindPass.objects.get(username=user.username).delete()
        
        del request.session['findpasser']
        return render_to_response('reset_password_success.html')
    else:
        return render_to_response('404.html')
    else:
        



# Create your views here.
