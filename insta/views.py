from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
# from django.views.generic import (
#     ListView
# )
from .forms import CommentForm, UserDetailForm, PostForm
from .models import Post, Comment, UserDetail
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# # Create your views here.
# class PostListView(ListView):
#     template_name = "home.html"
#     QuerySet = Post.objects.all()
#     context_object_name = 'posts'

def postview(request):
    
    return render(request, 'home.html')

def comment(request):
    if request.method == "POST":
        form =CommentForm(data= request.POST)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render( request,'home.html', {"obj": obj})

    else:
        forms = CommentForm()
        picture = Comment.objects.all()
    
    return render(request, 'comment.html', {"form":forms, "comment":comment})

def profile(request):
    if request.method == "POST":
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('home')

    else:
        form = UserDetailForm()
    userdetails = UserDetail.objects.all()
    
    return render(request, 'profile/profile.html', {"userdetails":userdetails,"form":form}) 

def post(request):
    if request.method == "POST":
        form =PostForm(data= request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render( request,'profile/update.html', {"obj": obj})

    else:
        forms = PostForm()
        picture = Post.objects.all()
    

    return render(request, 'profile/update.html', {"form":forms, "picture":picture})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save()
        return redirect('/login')
    context ={"form":form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
            form = AuthenticationForm(request)
    context = {"form":form}
    return render(request, 'accounts/login.html',context)
def logout_view(request):
    return render(request, 'accounts/logout.html')