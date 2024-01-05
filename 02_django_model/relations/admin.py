from django.contrib import admin

from .models import Address, Product, Profile

# Register your models here.


admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Profile)