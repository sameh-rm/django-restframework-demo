from re import L
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import validate_email

from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"
        # exclude = ("user",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", ]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, vd: dict):
        # vd stands for serializer validated_data
        user = User.objects.create_user(
            username=vd['username'],
            email=vd["email"],
            password=vd["password"]
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # username or email
    password = serializers.CharField()

    def validate(self, data):
        """
        returns serializer validated_data
        """
        username = data['username']
        password = data["password"]
        if username:
            try:
                validate_email(username)
                username = User.objects.get(email=data['username']).username
            except ValidationError:
                import sys
                print(sys.exc_info())
            user = authenticate(username=username, password=password)
        else:
            raise serializers.ValidationError(
                "Please enter username or email.")

        if user and user.is_active:
            return user

        raise serializers.ValidationError("Incorrect Credentials")
