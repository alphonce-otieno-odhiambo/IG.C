from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
# from django.views.generic import (
#     ListView
# )
from .forms import CommentForm, UserDetailForm
from .models import Post, Comment, UserDetail

# # Create your views here.
# class PostListView(ListView):
#     template_name = "home.html"
#     QuerySet = Post.objects.all()
#     context_object_name = 'posts'

def postview(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render (request, 'home.html', context)

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