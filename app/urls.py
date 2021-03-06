from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url('^index/$',views.index,name = "index"),	
	url('^sell/$',views.sell,name = "sell"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)