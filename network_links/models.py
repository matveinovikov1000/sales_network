from django.db import models

from products.models import Product


class Link(models.Model):
    """Модель звена сети"""

    FIRST_TITLE = "Завод"
    SECOND_TITLE = "Розничная сеть"
    THIRD_TITLE = "Индивидуальный предприниматель"

    TITLE_CHOICES = [
        (FIRST_TITLE, "Завод"),
        (SECOND_TITLE, "Розничная сеть"),
        (THIRD_TITLE, "Индивидуальный предприниматель"),
    ]

    title = models.CharField(
        max_length=30,
        choices=TITLE_CHOICES,
        default=FIRST_TITLE,
        verbose_name="Название звена сети",
        help_text="Укажите название звена сети",
    )
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите адрес электронной почты"
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Название страны дислокации звена сети",
        help_text="Укажите страну дислокации звена сети",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Название города дислокации звена сети",
        help_text="Укажите город дислокации звена сети",
    )
    street = models.CharField(
        max_length=50,
        verbose_name="Название улицы дислокации звена сети",
        help_text="Укажите улицу дислокации звена сети",
    )
    house_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Название улицы дислокации звена сети",
        help_text="Укажите улицу дислокации звена сети",
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
        verbose_name="Продукты",
        help_text="Укажите продукты",
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Поставщик",
        help_text="Укажите поставщика",
    )
    supplier_level = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Уровень поставщика",
        help_text="Укажите уровень поставщика",
    )
    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=None,
        verbose_name="Задолженность перед поставщиком",
        help_text="Укажите задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
        ordering = [
            "title",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "supplier_level",
            "debt",
            "created_at",
        ]

    def __str__(self):
        return self.title
