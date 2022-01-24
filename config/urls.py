from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls", namespace="api_accounts")),
    path("api/posts/", include("posts.urls", namespace="api_posts")),
    path("__debug__/", include("debug_toolbar.urls")),
]
