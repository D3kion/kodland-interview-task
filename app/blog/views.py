from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm


def index(req):
    posts = Post.objects.order_by('-pub_date')[:10]
    ctx = {
        'last_post': posts.first(),
        # Triplets of posts (Horrible hard code)
        'posts': [posts[1:4], posts[4:7], posts[7:10]],
    }

    return render(req, 'blog/index.html', ctx)


def create_post(req):
    if req.method == 'POST':
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            obj = Post.objects.create(
                title=name,
                content=content,
                image=image,
            )
            obj.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Bad Request', status=400)
    elif req.method == 'GET':
        return render(req, 'blog/create_post.html')
    else:
        return HttpResponse('Method Not Allowed', status=405)
