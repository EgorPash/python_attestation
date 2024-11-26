from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from customers.apps import CustomersConfig
from customers.views import CustomUserCreateAPIView

app_name = CustomersConfig.name

urlpatterns = [
    path("register/", CustomUserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)),name="token_refresh"),
]