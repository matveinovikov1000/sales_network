from rest_framework import generics

from products.serializers import ProductSerializer
from products.models import Product
from users.permissions import IsActive


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Показывает конкретный продукт"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductListAPIView(generics.ListAPIView):
    """Показывает список продуктов"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductCreateAPIView(generics.CreateAPIView):
    """Создает продукт"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Изменяет свойтсва продукита"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Удаляет продукт"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)
