from django.shortcuts import render,redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request,"a/index.html",{'user':request.user,'posts':posts})
    else:
        posts = Post.objects.all()
        return render(request,"a/index.html",{'posts':posts})

def login_user(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=uname,password=password)
        if user:
            login(request,user)
            return redirect("index")
        else:
            messages.error(request,"Username or Password Invalid")
    return render(request,"a/login.html",{})

def register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        user = User.objects.filter(username=uname,email=email)
        if user.exists():
             messages.error(request,"User Already Exists") 
        else:
            hashed_pass = make_password(password)
            user = User(username=uname,password=hashed_pass,first_name=first_name,last_name=last_name,email=email)
            user.save()
            messages.success(request,"User Created Successfully ")
    return render(request,"a/register.html",{})

def addpost(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = Post.objects.filter(title=title,author=request.user)
        if post.exists():
            messages.error(request,"Another Post with same title exists ")
        else:
            post = Post(title=title,content=content,author=request.user)
            post.save()
            messages.success(request,"Post Added Successfully")
    return render(request,"a/addpost.html",{})

def specific(request,id):
    post = Post.objects.get(id=id)
    return render(request,"a/specific.html",{'post':post})

def anything(request,string):
    data = "You Typed "+string+" in the search box &#128512"
    return HttpResponse(data)

def logout_user(request):
    logout(request)
    return redirect("index")