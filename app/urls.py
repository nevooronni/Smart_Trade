from django.urls import path,re_path
from django.conf import settings
from . import views

urlpatterns=[
	re_path('^$',views.landing_page,name="landing_page"),
	re_path(r'', views.index, name="index"),




]
