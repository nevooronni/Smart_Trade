from django.db import models
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
    phone_number = PhoneNumberField()
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

class Item(models.Model):
    cart = models.ForeignKey('Cart', on_delete = models.CASCADE, related_name = 'cart')
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, related_name= 'content_type')
    object_id = models.PositiveIntegerField()

    #objects = ItemManager()

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

    product = property(get_product, set_product)




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
