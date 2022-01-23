from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls", namespace="api/accounts/")),
    path("__debug__/", include("debug_toolbar.urls")),
]
