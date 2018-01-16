from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url(r'', views.index, name="index")
	path('product/', views.ProductDetailtView.as_view(), name='product'),


]
