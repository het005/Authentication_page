from django.shortcuts import render,redirect

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login


# Create your views here.

#user=het@
#paaword=het10526

def home(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,"index.html")

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html")
    return render(request, "login.html")
def logoutuser(request):
    logout(request)
    return redirect("/loginuser")