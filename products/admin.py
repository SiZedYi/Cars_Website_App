from django.contrib import admin
from .models import Brand, Type, Product, Country

# Register your models here.
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Country)