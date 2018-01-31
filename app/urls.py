from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url(r'^profile/$',views.profile,name = 'profile'),
	url(r'^futures/$',views.futures,name = 'futures'),
	url('^index/$',views.index,name = "index"),	
	url(r'^sell/$',views.sell,name = 'sell'),
	url(r'^buy/$',views.buy,name = 'buy'),
	url(r'^buy_sugar/$',views.buy_sugar,name = 'buy_sugar'),
	url(r'^buy_coffee/$',views.buy_coffee,name = 'buy_coffee'),
	url(r'^buy_cotton/$',views.buy_cotton,name = 'buy_cotton'),
	url(r'^sell_sugar/$',views.sell_sugar,name = 'sell_sugar'),
	url(r'^sell_coffee/$',views.sell_coffee,name = 'sell_coffee'),
	url(r'^sell_cotton/$',views.sell_cotton,name = 'sell_cotton'),
	url(r'^place_order/$',views.place_order,name = 'place_order'),
	url(r'^remove_item/(\d+)',views.remove_item,name = 'remove_item'),
	#url(r'^cart/', views.get_cart, name= "cart"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
