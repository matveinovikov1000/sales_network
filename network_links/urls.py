from django.urls import path

from network_links.apps import NetworkLinksConfig
from network_links.views import (
    LinkRetrieveAPIView,
    LinkListAPIView,
    LinkCreateAPIView,
    LinkUpdateAPIView,
    LinkDestroyAPIView,
)

app_name = NetworkLinksConfig.name

urlpatterns = [
    path("link/<int:pk>/", LinkRetrieveAPIView.as_view(), name="link"),
    path("links/", LinkListAPIView.as_view(), name="links"),
    path("create_link/", LinkCreateAPIView.as_view(), name="create_link"),
    path("update_link/<int:pk>/", LinkUpdateAPIView.as_view(), name="update_link"),
    path("delete_link/<int:pk>/", LinkDestroyAPIView.as_view(), name="delete_link"),
]
