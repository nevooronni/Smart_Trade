from django.shortcuts import render,redirect
from .forms import SellForm,CoffeeForm
from django.conf.urls import url
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Wheat,Profile,Cart,ItemManager,Item,Buyer,Sell,Category,Coffee
from .cart import *
from django.views import generic
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = '/accounts/login/')
def landing_page(request):
    #wheat
    wheat_products = Wheat.get_all_wheat_sales()
    lowest_price = Wheat.get_lowest_price()
    print(lowest_price.get("unit_price__min"))
    price = lowest_price.get("unit_price__min")


        # wheat_prices = []
        # for p in wheat_products:
        #     price_list = wheat_prices.append(p.unit_price)
        # return price_list
        # lowest = min(wheat_prices)
        # product_prices = []
        # for p in products:
        #     product_prices.append(p.unit_price)
        #     lowest = min(product_prices)
        # return lowest

    current_user = request.user
    current_profile = current_user.profile 

    if request.method == 'POST':
        form = SellForm(request.POST,request.FILES)

        if form.is_valid():
            sell = form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        form = SellForm()     


    coffee_products = Coffee.get_all_coffee_sales()
    lowest_price = Coffee.get_lowest_price()
    print(lowest_price.get("unit_price__min"))
    coffee_price = lowest_price.get("unit_price__min")

    current_user = request.user
    current_profile = current_user.profile

    if request.method == 'POST':
        coffee_form = CoffeeForm(request.POST,request.FILES)

        if coffee_form.is_valid():
            sell = coffee_form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        coffee_form = CoffeeForm()

    return render(request,'all-app/landing_page.html',{"wheat_products":wheat_products,"price":price,"form":form,"coffee_products":coffee_products,"coffee_price":coffee_price,"coffee_form":coffee_form,"current_user":current_user,})

@login_required(login_url = '/accounts/login/')
def index(request):
	return render(request,'all-app/index.html')

@login_required(login_url = '/accounts/login/')
def sell(request):
    current_user = request.user
    current_profile = current_user.profile 

    if request.method == 'POST':
        form = SellForm(request.POST,request.FILES)

        if form.is_valid():
            sell = form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        form = SellForm()

    if request.method == 'POST':
        coffee_form = CoffeeForm(request.POST,request.FILES)

        if coffee_form.is_valid():
            sell = coffee_form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        coffee_form = CoffeeForm()

    return render(request,'all-app/sell.html',{"form":form,"coffee_form":coffee_form,"current_user":current_user,})

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

	
