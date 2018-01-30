from django.shortcuts import render,redirect
from .forms import SellForm,CoffeeForm,SugarForm,CottonForm,CartItemForm
from django.conf.urls import url
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Wheat,Profile,CartItem,ItemManager,Item,Buyer,Sell,Category,Coffee,Sugar,Cotton
from .cart import *
from django.views import generic
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = '/accounts/login/')
def profile(request):
    # current_user = request.user

    # print('Logged In')
    # profile = Profile.objects.filter(user=current_user)

    # current_profile = current_user.profile
    # account_balance = current_user.profile.account

    # cartitems = CartItem.get_all_cartitems()
    # total = CartItem.get_total_price()
    # print(total.get("subtotal__sum"))
    # total_cost = total.get("subtotal__sum")

    # transaction_cost = total_cost + (total_cost * 0.05)

    # if transaction_cost <= account_balance:
    #     new_account_balance = account_balance - transaction_cost
       
    # else:
    #     please_topup = "Sorry you do not have enough funds in your account to complete the transaction please topup to continue!"

    #     return HttpResponse(please_topup)  

    return render(request, 'all-app/profile.html', )   


@login_required(login_url = '/accounts/login/')
def landing_page(request):
    #buy forms 
    buy_form = CartItemForm()


    #wheat
    wheat_products = Wheat.get_all_wheat_sales()
    lowest_price = Wheat.get_lowest_price()
    print(lowest_price.get("unit_price__min"))
    price = lowest_price.get("unit_price__min")
    # retail_price = (price * 5/100) + price

    def change(price):
        list_prices = []
        list_prices.append(price)
        print(list_prices)
        change = list_prices[-1] - list_prices[-2]
        
        return change
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

    sugar_products = Sugar.get_all_sugar_sales()
    lowest_price = Sugar.get_lowest_price()
    print(lowest_price.get("unit_price__min"))
    sugar_price = lowest_price.get("unit_price__min")

    current_user = request.user
    current_profile = current_user.profile

    if request.method == 'POST':
        sugar_form = SugarForm(request.POST,request.FILES)

        if sugar_form.is_valid():
            sell = sugar_form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        sugar_form = SugarForm()

    cotton_products = Cotton.get_all_cotton_sales()
    lowest_price = Cotton.get_lowest_price()
    print(lowest_price.get("unit_price__min"))
    cotton_price = lowest_price.get("unit_price__min")

    current_user = request.user
    current_profile = current_user.profile

    if request.method == 'POST':
        cotton_form = CottonForm(request.POST,request.FILES)

        if cotton_form.is_valid():
            sell = cotton_form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        cotton_form = CottonForm()

    cartitems = CartItem.get_all_cartitems()
    total = CartItem.get_total_price()
    print(total.get("subtotal__sum"))
    total_cost = total.get("subtotal__sum")

    return render(request,'all-app/landing_page.html',{"total_cost":total_cost,"cartitems":cartitems,"wheat_products":wheat_products,"change":change,"price":price,"form":form,"buy_form":buy_form,"coffee_products":coffee_products,"coffee_price":coffee_price,"coffee_form":coffee_form,"sugar_price":sugar_price,"sugar_form":sugar_form,"cotton_form":cotton_form,"cotton_price":cotton_price,"current_user":current_user,})

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

    return render(request,'all-app/sell.html',{"form":form,"current_user":current_user,})

@login_required(login_url = '/accounts/login/')
def buy(request):
    current_user = request.user
    current_profile = current_user.profile

    wheat_name = 'wheat'
    lowest_price = Wheat.get_lowest_price()
    print(lowest_price.get("unit_price__min"))
    wheat_price = lowest_price.get("unit_price__min")


    if request.method == 'POST':
        buy_form = CartItemForm(request.POST,request.FILES)

        if buy_form.is_valid():
            buy = buy_form.save(commit=False)
            buy.user = current_user
            buy.profile = current_profile
            buy.name = wheat_name 
            buy.price = wheat_price 
            buy.subtotal = buy.price * buy.quantity
            buy.save()


            return redirect(landing_page)

        else:

            buy_form = CartItemForm()


@login_required(login_url = '/accounts/login/')
def remove_buy(request):
    current_user = request.user
    current_profile = current_user.profile  

@login_required(login_url = '/accounts/login/')
def sell_sugar(request):
    current_user = request.user
    current_profile = current_user.profile 

    if request.method == 'POST':
        sugar_form = SugarForm(request.POST,request.FILES)

        if sugar_form.is_valid():
            sell = sugar_form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        sugar_form = SugarForm()

@login_required(login_url = '/accounts/login/')
def sell_coffee(request):
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

@login_required(login_url = '/accounts/login/')
def sell_cotton(request):
    current_user = request.user
    current_profile = current_user.profile 

    if request.method == 'POST':
        cotton_form = CottonForm(request.POST,request.FILES)

        if cotton_form.is_valid():
            sell = cotton_form.save(commit=False)
            sell.user = current_user
            sell.profile = current_profile
            sell.save()

            return redirect(landing_page)
    else:

        cotton_form = CottonForm()

@login_required(login_url = '/accounts/login/')
def remove_item(request,id):
    current_user = request.user
    current_profile = current_user.profile 

    item_removed = CartItem.remove_cartitem(id=id)

    return redirect(landing_page)

@login_required(login_url = '/accounts/login/')
def place_order(request):
    current_user = request.user
    current_profile = current_user.profile 
    # profile = Profile.objects.filter(user=current_user)
    account_balance = current_profile.account
    print(account_balance)

    cartitems = CartItem.get_all_cartitems()
    total = CartItem.get_total_price()
    print(total.get("subtotal__sum"))
    total_cost = total.get("subtotal__sum")

    transaction_cost = total_cost + (total_cost * 0.05)
    print(transaction_cost)

    if transaction_cost <= account_balance:
        balance = account_balance - transaction_cost
        new_account_balance = int(balance)
        account_balance = new_account_balance
        print(account_balance)

        p = Profile.objects.get(user=current_user)
        p.account = account_balance
        print(p.account)
        p.save()

        return redirect(landing_page)

    else:
        please_topup = "Sorry you do not have enough funds in your account to complete the transaction please topup to continue!"

        return HttpResponse(please_topup)   

    return redirect(landing_page) 

