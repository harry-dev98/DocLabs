from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import UserData
# Create your views here.
def index(request):
    datas=UserData.objects.all()
    return render(request,"index.html",{'datas':datas})


def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html",{'message':"wrong credentials"}) 
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('index')   