from django.db.models.query import QuerySet
from django.shortcuts import render
# from django.views.generic import (
#     ListView
# )
from .forms import CommentForm
from .models import Post

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
    if request.method =="POST":
        form = CommentForm(data = request.POST)
        if form.is_valid():
            form.save()
            return render('home')
    else:
        form = CommentForm()
    context = {"form":form}
    return render(request, 'comment.html', context)