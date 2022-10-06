from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-time_creation']

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'