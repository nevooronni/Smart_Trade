from django.shortcuts import render,redirect
from django.conf.urls import url 
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = '/accounts/login/')
def landing_page(request):
	return render(request,'all-app/landing_page.html')

@login_required(login_url = '/accounts/login/')
def index(request):
	return render(request,'all-app/index.html')

@login_required(login_url = '/all-app/sell')
def sell(request):
	
	return render(request,'all-app/sell.html')