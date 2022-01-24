from django.contrib.auth import get_user_model
from django.db.models import Count, Prefetch
from django.urls import path
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts import serializers, views

# from categories.models import Category
from posts.models import Post

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
            serializer_class=serializers.UserWithPostsSerializer,
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
    path(
        "users-with-posts-and-categories-filtered-by-category",
        generics.ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related(
                # Prefetch(
                #     "posts__categories", queryset=Category.objects.filter(name="python")
                # )
                # Prefetch(
                #     "posts",
                #     queryset=Post.objects.prefetch_related("categories").filter(
                #         categories__name__in=["python"]
                #     )
                # )
                Prefetch(
                    "posts",
                    queryset=Post.objects.annotate(categories_count=Count("categories"))
                    .prefetch_related("categories")
                    .filter(categories__name__in=["python"], categories_count=1),
                )
            ),
            serializer_class=serializers.UserWithPostsAndCategoriesSerializer,
        ),
        name="user_with_posts_and_categories",
    ),
    path(
        "top-10-users-by-post-count/",
        generics.ListAPIView.as_view(
            queryset=User.objects.annotate(posts_count=Count("posts")).order_by(
                "-posts_count"
            )[0:10],
            serializer_class=serializers.UsersWithPostCountSerializer,
            pagination_class=None,
        ),
        name="top-10-users-by-post-count",
    ),
]
