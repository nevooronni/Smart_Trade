from django.contrib import admin
from .models import Product,Wheat,Coffee,Sugar,Cotton,wheat_futures

admin.site.register(Product)
admin.site.register(Wheat)
admin.site.register(Coffee)
admin.site.register(Sugar)
admin.site.register(Cotton)
admin.site.register(wheat_futures)
