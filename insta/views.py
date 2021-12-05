from django.db.models.query import QuerySet
from django.shortcuts import render
# from django.views.generic import (
#     ListView
# )
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