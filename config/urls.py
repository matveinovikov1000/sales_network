from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("network_links/", include("network_links.urls", namespace="network_links")),
    path("products/", include("products.urls", namespace="products")),
]
