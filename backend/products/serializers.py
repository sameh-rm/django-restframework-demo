from django.db.models import fields
from rest_framework import serializers
from .models import (Product, Category, Image, Variant, VariantOption)


class PrductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ("owner",)

    # def create(self, vd):
    #     vd["owner"] = self.request.user
