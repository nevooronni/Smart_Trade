from django.shortcuts import render,redirect
from django.conf.urls import url
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Item,Cart,Profile
from django.views import generic
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required


def landing_page(request):
	return render(request,'all-app/landing_page.html')

@login_required(login_url='/accounts/login')
def index(request):
	all_products = Product.get_all_products()
	return render(request, 'index.html',{"products": all_products})  
