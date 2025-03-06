from rest_framework import generics

from users.serializers import UserSerializer
from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Сохраняет пользователя и хэширует пароль"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
