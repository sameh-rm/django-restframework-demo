from django.contrib import admin
from .models import Category, Image, Offer, Product, Variant, VariantOption
# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Offer)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(VariantOption)
