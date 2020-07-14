from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def home(request):
    return render(request,"case_form.html")


def register(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password_field']
        password2=request.POST['confirm_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken")
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save();
        else:
            messages.info(request,"Password doesn't match")
            return redirect('/')
        return redirect('/login')
    else:
        return render(request,'authentication_app/register.html')


def login(request):
    if request.method=="POST":
        username
    else:
        return render(request,'authentication_app/login.html')

