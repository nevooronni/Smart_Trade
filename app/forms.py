from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Wheat,Coffee,Sugar,Cotton

class SellForm(forms.ModelForm):
	class Meta:
		model = Wheat
		fields = ('unit_price','quantity',)

class CoffeeForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields = ('unit_price','quantity',)

class SugarForm(forms.ModelForm):
	class Meta:
		model = Sugar
		fields = ('unit_price','quantity',)

class CottonForm(forms.ModelForm):
	class Meta:
		model = Cotton
		fields = ('unit_price','quantity',)

class BuyForm(forms.ModelForm):
	class Meta:
		model = Wheat
		fields = ('quantity',)