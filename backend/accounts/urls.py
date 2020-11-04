from django.urls import include, path
from knox import views as knox_views
from .api import LoginAPI, RegisterAPI, UserAPI
urlpatterns = [
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
    path('auth/user', UserAPI.as_view()),
    # path(r'knox', include('knox.urls'))

]
