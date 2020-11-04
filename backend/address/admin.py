from .models import Address, BillingAddress, ShippingAddress
from django.contrib import admin

# Register your models here.

admin.site.register(Address)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
