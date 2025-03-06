from rest_framework import generics
from rest_framework.filters import SearchFilter

from network_links.serializers import LinkSerializer
from network_links.models import Link
from users.permissions import IsActive


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    """Выводит конкретное звено сети"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsActive,)


class LinkListAPIView(generics.ListAPIView):
    """Выводит список звеньев сети"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filter_backends = [
        SearchFilter,
    ]
    search_fields = [
        "country",
    ]
    permission_classes = (IsActive,)


class LinkCreateAPIView(generics.CreateAPIView):
    """Создает звено сети"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsActive,)

    def perform_create(self, serializer):
        """Устанавливает уровень звена сети в зависимости от поставщика"""
        link = serializer.save()

        if link.title == "Завод":
            link.supplier_level = 0

        if link.supplier != 1:
            link.supplier_level = 2
        elif link.supplier == 1:
            link.supplier_level = 1

        link.save()


class LinkUpdateAPIView(generics.UpdateAPIView):
    """Изменяет свойства звена сети"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsActive,)

    def perform_update(self, serializer):
        """Запрещает менять сумму задоженности через CRUD"""
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
            raise Exception("Менять сумму задолженности запрещено")
        super().perform_update(serializer)


class LinkDestroyAPIView(generics.DestroyAPIView):
    """Удаляет звено сети"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsActive,)
