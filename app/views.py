from django.shortcuts import render, redirect
from django.conf.urls import url
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.


def landing_page(request):
    return render(request, 'all-app/landing_page.html')


def post(request, pk):
    post = Post.objects.get(pk=post_id)

    return render(request, 'all-app/post.html')
