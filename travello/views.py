from django.shortcuts import render,redirect
from .models import destination
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,"index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password1 = request.POST["password"]
        password2 = request.POST["password1"]
        if password1 == password2  :
            if User.objects.filter(username = username).exists():
                messages.info(request,"username is same")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"same password")
            return redirect("register")
    else:
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"user not exist")
            return redirect("login") 
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return render(request,"index.html")
   
def save(request):
    name = request.POST["name"]
    user = destination(name=name)
    user.save()
    uu = destination.objects.all()
    return render(request,"index.html",{"us":uu})
    