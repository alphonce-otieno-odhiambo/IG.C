from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
# from django.views.generic import (
#     ListView
# )
from .forms import CommentForm, UserDetailForm, PostForm
from .models import Post, Comment, UserDetail, FollowersCount
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
    profile_det = UserDetail.objects.all()
    # adding context 
    ctx = {'photo':profile_det}
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
        form.save()
        return redirect('login',{})

    else:
        form = UserCreationForm()
    context ={"form":form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method =="POST":
        login_form = AuthenticationForm(request, data = request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            user.save()
            return redirect('/')
    else:
        login_form = AuthenticationForm(request)
    context = {"login_form":login_form}
    return render(request, 'login.html', context)

def logout_view(request):
    return render(request, 'accounts/logout.html')

def followercount(request):
    if request.method =="POST":
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == "follow":
            follower_cnt = FollowersCount.objects.create(follower = follower, user = user)
            follower_cnt.save()
            return redirect('/?user='+user)
    return render(request, 'follows/index.html',)
    

def index(request):
    current_user = request.GET.get('user')
    logged_in_user = request.user.username
    user_follower = len(FollowersCount.objects.filter(user = current_user))
    user_following = len(FollowersCount.objects.filter(follower = current_user))
    return render(request, 'follows/index.html', {
        "current_user":current_user,
        "user_follower":user_follower,
        "user_following":user_following
    })