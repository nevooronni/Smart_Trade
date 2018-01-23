from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Sell

class SellForm(forms.):
	class Meta:
		model = Sell
		fields = ('unit_price','quantitiy',)