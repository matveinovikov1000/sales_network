from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    "Модель пользователя"

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите ваш Email"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "email",
        ]

    def __str__(self):
        return self.email
