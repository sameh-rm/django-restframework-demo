from django.urls import include, path
from knox import views as knox_views
from .api import LoginAPI, RegisterAPI, UserAPI
from rest_framework.routers import DefaultRouter
from .api import AddressViewSet
router = DefaultRouter()
router.register(r"auth/user/address", AddressViewSet, basename="address")

urlpatterns = [
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
    path('auth/logoutall', knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    path('auth/user', UserAPI.as_view()),
    # path(r'knox', include('knox.urls'))

]
urlpatterns += router.urls
