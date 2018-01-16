from django.shortcuts import render, redirect
from django.conf.urls import url
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .email import send_welcome_email
from django.shortcuts import render, redirect
from django.conf.urls import url
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Product, Profile

# Create your views here.


def landing_page(request):
    return render(request, 'all-app/landing_page.html')


def post(request, pk):
    post = Post.objects.get(pk=post_id)

    return render(request, 'all-app/post.html')


def index(request):
    all_products = Product.get_all_products()
    return render(request, 'index.html', {"products": all_products})
