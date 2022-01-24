from django.urls import path
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts import views, serializers

User = get_user_model()


app_name = "api/accounts/"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("token/login/", views.LoginView.as_view(), name="token_login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path(
    #     "users-with-posts/", views.UserWithPostsView.as_view(), name="users_with_posts"
    # ),
    path(
        "users-with-posts/",
        generics.ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related("posts"),
            serializer_class=serializers.UserWithPostsAndCategoriesSerializer,
        ),
        name="users_with_posts",
    ),
    # path(
    #     "users-with-posts-and-categories/",
    #     views.UserWithPostAndCategoriesView.as_view(),
    #     name="user_with_posts_and_categories",
    # ),
    path(
        "users-with-posts-and-categories/",
        generics.ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related("posts__categories"),
            serializer_class=serializers.UserWithPostsAndCategoriesSerializer,
        ),
        name="user_with_posts_and_categories",
    ),
]
