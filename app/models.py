from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=140, blank=True)
    last_name = models.CharField(max_length=140, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = PhoneNumberField(max_length = 10, blank = True)
    location = models.CharField(max_length=140, blank=True)
    email = models.EmailField(max_length=140, blank=True)

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)

class Wheat(models.Model):
    name = models.CharField(max_length=140)
    quantity = models.IntegerField()
    price  =  models.IntegerField()
    unit_price = models.IntegerField()
    product_image = models.ImageField(upload_to='products',blank=True)
    description = models.TextField(blank=True)

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

class Buyer(models.Model):
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


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'category')
    name = models.CharField(max_length=140, blank=True)
    description = models.CharField(max_length=140, blank=True)

    @classmethod
    def display_categories(cls):
        categories = cls.objects.all()
        return categories

    @classmethod
    def get_single_category(cls,pk):
        category = cls.objects.get(pk=pk)
        return category

    def __str__(self):
        return self.name
class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)

class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)

class Item(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='item')
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE, related_name='item')
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

       