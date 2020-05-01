from django.shortcuts import render

from .models import Post


def index(req):
    latest_posts = Post.objects.order_by('-pub_date')[:10]
    return render(req, 'blog/index.html', {'posts': latest_posts})


def create_post(req):
    return render(req, 'blog/create_post.html')
