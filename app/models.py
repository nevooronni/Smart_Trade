from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
# from email_field.modelfields import EmailField


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = PhoneNumberField()
    locatiom = models.CharField(max_length=140, blank=True)
    email = models.EmailField(max_length=140, blank=True)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    post_save.connect(create_user_profile, sender=User)


class Product(models.Model):
    name = models.CharField(max_length=140, blank=True)
    unit_quantity = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    category = models.CharField(max_length=140, blank=True)
    description = models.TextField(max_length=140)

    class Meta:
        ordering = ['category']

    @classmethod
    def get_all_products(cls):
        products = cls.objects.all()
        return products

    @classmethod
    def get_single_product(cls, pk):
        product = cls.objects.get(pk=pk)
        return product

    @classmethod
    def display_users_products(cls, id):
        products = cls.objects.filter(user_id=id)
        return products

    def get_absolute_url(self):
        """
        Returns the url to access a particular product instance.
        """
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
