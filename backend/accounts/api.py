from rest_framework.exceptions import NotFound
from .models import Address
from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import (LoginSerializer, UserSerializer,
                          RegisterSerializer, AddressSerializer)
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


# Create your views here.


class AddressViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer

    def create(self, request):
        if request.user:
            request.data["user"] = request.user.id
        return super().create(request)

    def update(self, request, pk=None):
        if request.user:
            request.data["user"] = request.user.id
        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        if request.user:
            request.data["user"] = request.user.id
        return super().partial_update(request, pk)

    def get_queryset(self):
        return self.request.user.address_set

    def retrieve(self, request, pk=None):
        try:
            instance = request.user.address_set.get(id=pk)
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Address.DoesNotExist:
            return Response(
                {"message": "This address is not found in your address's list!", "status_code": 404}, 404)
