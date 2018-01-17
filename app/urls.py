from django.conf.urls import url 
from django.conf import settings
from . import views 

urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url('^index/$',views.index,name = "index"),	
]