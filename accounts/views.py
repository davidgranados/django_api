from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import serializers


class LoginView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer
