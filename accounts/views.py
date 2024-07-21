from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"user already exist ")
            return redirect("/auth/register/")
        user=User.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        messages.info(request,"user created successfully")
        return redirect("/auth/register/")
    template=loader.get_template('register.html')
    context={}
    return HttpResponse(template.render(context,request))
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if(not User.objects.filter(username=username)):
            messages.info(request,"user does not exist")
            return redirect('/auth/login')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"invalid password")
            return redirect('/auth/login')
        login(request,user)
        messages.info(request,'login Succesfully')
        return redirect('/porblems/all/')
    template=loader.get_template('login.html')
    context={}
    return HttpResponse(template.render(context,request))
def log_out(request):
    logout(request)
    messages.info(request,'logout Succesfully')
    return redirect('/auth/login')