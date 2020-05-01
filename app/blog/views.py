from django.shortcuts import render

from .models import Post


def index(req):
    posts = Post.objects.order_by('-pub_date')[:10]
    ctx = {
        'last_post': posts.first(),
        # Triplets of posts (Horrible hard code)
        'posts': [posts[1:4], posts[4:7], posts[7:10]],
    }

    return render(req, 'blog/index.html', ctx)


def create_post(req):
    return render(req, 'blog/create_post.html')
