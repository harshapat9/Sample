from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    email = request.POST['email']
    password = request.POST['password']
    user_obj = user.objects.filter(email=email, password=password).exists()
    if user_obj:
        return HttpResponse("Login Success")
    return render(request,'register.html',{
        "message" : "Account Not found, register"
    })

    # return redirect('register')
    

def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    email = request.POST['email']
    password = request.POST['password']
    user.objects.create(email = email, password = password)
    return render(request, 'login.html', {
        "message" : "Account Created!"
    })
    # return redirect('login')


def base(request):
    return render(request,'base.html')