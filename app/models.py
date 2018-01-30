from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.db.models import Avg, Max, Min, Sum
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum, F

import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=140, blank=True)
    last_name = models.CharField(max_length=140, blank=True)
    phone_number = PhoneNumberField(max_length = 10, blank = True)
    location = models.CharField(max_length=140, blank=True)
    email = models.EmailField(max_length=140, blank=True)
    account = models.IntegerField(default=10000)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)#creates a profile when creating a user

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()#save a profile when saving a user

@property
def photo_url(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url

class Wheat(models.Model):
    futures = models.ForeignKey(Futures, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    sell_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    class Meta:
        ordering = ['-sell_time']

    @classmethod
    def get_all_wheat_sales(cls):
        all_wheat = cls.objects.all()
        return all_wheat

    @classmethod
    def get_total_amount(cls):
        total_amount = cls.objects.filter(<filters>).aggregate(Sum(F('unit_price')*F('quantity')))

        return total_amount

    @classmethod
    def get_lowest_price(cls):
        lowest_price = cls.objects.all().aggregate(min('unit_price'))
        return lowest_price

    @classmethod
    def get_single_wheat(cls,pk):
        single_wheat  = cls.objects.filter(pk=pk)


class Coffee(models.Model):
    futures = models.ForeignKey(futures,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    sell_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    class Meta:
        ordering = ['-sell_time']

    @classmethod
    def get_all_coffee_sales(cls):
        all_coffee = cls.objects.all()
        return all_coffee

    @classmethod
    def get_total_amount(cls):
        total_amount = cls.objects.filter(<filters>).aggregate(Sum(F('unit_price')*F('quantity')))

        return total_amount

    @classmethod
    def get_lowest_price(cls):
        lowest_price = cls.objects.all().aggregate(min('unit_price'))
        return lowest_price

    @classmethod
    def get_single_wheat(cls,pk):
        single_wheat  = Coffee.objects.filter(pk=pk)

    @classmethod
    def get_user_wheat(cls,user_id):
        user_coffee = cls.objects.filter(user=user.id).all()
        return user_coffee

class Product(models.Model):
    name = models.CharField(max_length=140)
    quantity = models.IntegerField()
    price  =  models.IntegerField()
    unit_price = models.IntegerField()
    product_image = models.ImageField(upload_to='products',blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    class Meta:
        ordering  = ['name']

    @classmethod
    def get_product_by_name(cls,name):
        products = Product.objects.filter(name=name).all()
        return products

    @classmethod
    def display_buyersy_products(cls):
        products = cls.objects.all()
        return products

    @classmethod
    def get_single_prodcut(cls,pk):
        product = cls.objects.get(pk=pk)
        return product

    def __str__(self):
        return self.name

class Sell(models.Model):

    account_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'sell')
    product =  models.ForeignKey(Product,on_delete=models.CASCADE, related_name= 'sell')


    @classmethod
    def get_single_product(cls,pk):
        sell = cls.objects.get(pk=pk)
        return sell


    @classmethod
    def display_buyers(cls):
        buyers = cls.objects.all()
        return buyers

    @classmethod
    def get_single_buyer(cls,pk):
        buyer = cls.objects.get(pk=pk)
        return buyer

    def __str__(self):
        return self.name

class Buy(models.Model):
    name = models.CharField(max_length=140, blank= True)
    account_number = models.IntegerField()

    @classmethod
    def display_sellers(cls):
        sellers = cls.objects.al()
        return sellers

    @classmethod
    def get_single_seller(cls,pk):
        seller = cls.objects.get(pk=pk)
        return seller

    def __str__(self):
        return self.name

class Futures(models.Model):
    name = models.CharField(max_length=40,blank=True)
