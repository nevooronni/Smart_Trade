from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Wheat

class SellForm(forms.ModelForm):
	class Meta:
		model = Wheat
		fields = ('unit_price','quantity',)