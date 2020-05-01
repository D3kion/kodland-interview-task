# from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('Blog')


def create_post(req):
    return HttpResponse('Create blog post')
