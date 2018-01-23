from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url(r'', views.index, name="index"),
<<<<<<< HEAD
=======
	#url(r'^cart/', views.get_cart, name= "cart")




>>>>>>> 88571435a32e8849f477f49959bf84682b22bade
]
