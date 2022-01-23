from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts import views

app_name = "api/accounts/"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("token/login/", views.LoginView.as_view(), name="token_login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
