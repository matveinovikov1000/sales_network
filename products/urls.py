from django.urls import path

from products.apps import ProductsConfig
from products.views import (
    ProductRetrieveAPIView,
    ProductListAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
)

app_name = ProductsConfig.name

urlpatterns = [
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product"),
    path("products/", ProductListAPIView.as_view(), name="products"),
    path("create_product/", ProductCreateAPIView.as_view(), name="create_product"),
    path(
        "update_product/<int:pk>/",
        ProductUpdateAPIView.as_view(),
        name="update_product",
    ),
    path(
        "delete_product/<int:pk>/",
        ProductDestroyAPIView.as_view(),
        name="delete_product",
    ),
]
