from django.db import models


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Укажите название продукта",
    )
    model = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название продукта",
        help_text="Укажите название продукта",
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата выхода продукта на рынок",
        help_text="Укажите дату выхода продукта на рынок",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "title",
            "model",
            "release_date",
        ]

    def __str__(self):
        return self.title
