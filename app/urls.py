from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

<<<<<<< HEAD
urlpatterns = [
    url('^$', views.landing_page, name="landing_page"),
    url('^index/$', views.index, name="index"),
    url(r'^sell/$', views.sell, name='sell'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^sell_sugar/$', views.sell_sugar, name='sell_sugar'),
    url(r'^sell_coffee/$', views.sell_coffee, name='sell_coffee'),
    url(r'^sell_cotton/$', views.sell_cotton, name='sell_cotton'),
    url(r'^profile/', views.profile, name="profile"),
    url(r'^search/', views.search_results, name='search_results'),
=======
urlpatterns=[
	url('^$',views.landing_page,name="landing_page"),
	url('^index/$',views.index,name = "index"),	
	url(r'^sell/$',views.sell,name = 'sell'),
	url(r'^buy/$',views.buy,name = 'buy'),
	url(r'^sell_sugar/$',views.sell_sugar,name = 'sell_sugar'),
	url(r'^sell_coffee/$',views.sell_coffee,name = 'sell_coffee'),
	url(r'^sell_cotton/$',views.sell_cotton,name = 'sell_cotton'),
	url(r'^place_order/$',views.place_order,name = 'place_order'),
	url(r'^remove_item/(\d+)',views.remove_item,name = 'remove_item'),
	#url(r'^cart/', views.get_cart, name= "cart"),
>>>>>>> f9ceec8d816b3947c3fe4da81d966e46db29bf92
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
