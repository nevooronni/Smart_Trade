from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Sell,Product

class SellForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name','unit_price','quantity',)