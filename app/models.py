from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
# from email_field.modelfields import EmailField

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

class Product(models.Model):
	name = models.CharField(max_length=140, blank=True)

