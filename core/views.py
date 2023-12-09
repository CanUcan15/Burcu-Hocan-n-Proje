from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blogposts.models import Post

class HomeView(ListView):
    model = Post
    template_name = "core/index.html"

class ArticleDetailView(ListView):
    model = Post
    template_name = "core/article_details.html"