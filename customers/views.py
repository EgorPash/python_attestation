from django.contrib.auth.hashers import make_password

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from customers.models import CustomUser
from customers.serializers import CustomUserSerializer, MyTokenObtainPairSerializer


class CustomerViewSet(ViewSet):

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomUserCreateAPIView(CreateAPIView):

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data["password"]))

class MyTokenObtainPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer

