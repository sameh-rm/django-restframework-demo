from .models import Product
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from .serializers import PrductSerializer

User = get_user_model()


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PrductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        print("action:", self.action)
        if self.action in ('create', 'update', 'destroy', 'patch'):
            self.permission_classes = [permissions.IsAdminUser, ]
        return super(self.__class__, self).get_permissions()
