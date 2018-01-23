from django.shortcuts import render,redirect
from django.conf.urls import url
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Product,Profile,Cart,ItemManager,Item,Buyer,Seller,Category
from cart import *
from django.views import generic
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required





def landing_page(request):
	return render(request,'all-app/landing_page.html')

@login_required(login_url='/accounts/login')
def index(request):
	all_products = Product.objects.all()
	return render(request, 'index.html',{"products": all_products})

@login_required(login_url='/accounts/login')
def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

@login_required(login_url='/accounts/login')
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
@login_required(login_url='/accounts/login')
def get_cart(request):
    return render_to_response('cart.html', dict(cart=Cart(request)))
