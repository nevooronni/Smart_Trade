from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url(r'', views.index, name="index"),
	#url(r'^cart/', views.get_cart, name= "cart")




]
