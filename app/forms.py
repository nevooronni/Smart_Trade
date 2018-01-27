from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Wheat,Coffee

class SellForm(forms.ModelForm):
	class Meta:
		model = Wheat
		fields = ('unit_price','quantity',)

class CoffeeForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields = ('unit_price','quantity',)