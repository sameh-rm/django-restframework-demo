from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, User
from django.http import request
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import serializers, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
# Custom UserModel instead i can import my UserModel directly
User = get_user_model()
# Register API


class RegisterAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Get User API


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
