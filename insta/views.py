from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
# from django.views.generic import (
#     ListView
# )
from .forms import CommentForm, UserDetailForm, PostForm
from .models import Post, Comment, UserDetail
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# # Create your views here.
# class PostListView(ListView):
#     template_name = "home.html"
#     QuerySet = Post.objects.all()
#     context_object_name = 'posts'

def postview(request):
    photo = Post.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'home.html', ctx)

def comment(request):
    if request.method == "POST":
        form =CommentForm(data= request.POST)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render( request,'home.html', {"obj": obj})

    else:
        forms = CommentForm()
        comment = Comment.objects.all()
    
    return render(request, 'comment.html', {"form":forms, "comment":comment})

def profile_page(request):
    profile = UserDetail.objects.all()
    # adding context 
    ctx = {'photo':profile}
    
    return render(request, 'profile/profile_page.html', ctx)
def profile(request):
    if request.method == "POST":
        form = UserDetailForm(data=request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            object = form.instance
            return redirect('profile/profile.html', {"object":object})

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
        return redirect('/login', {"form_obj":form_obj})
    context ={"form":form,
                
    }
    return render(request, 'accounts/register.html', context)
@login_required
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

def followercount(request):
    return render()

def index(request):
    current_user = request.GET.get('user')
    logged_in_user = request.user.username
    return render(request, 'follows/index.html', {"current_user":current_user})