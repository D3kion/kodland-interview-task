from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create', views.create_post, name='create-post'),
]
