from django.contrib import admin

# Register your models here.
from .models import Product, Breadcrumb

admin.site.register(Product)
admin.site.register(Breadcrumb)
