from django.contrib import admin

from network_links.models import Link


@admin.action(description="Обнулить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    """Обнуляет задолженность перед поставщиком"""
    queryset.update(debt=0.00)


@admin.register(Link)
class LinkModelAdmin(admin.ModelAdmin):
    """Отображает звенья сети в админке"""

    list_display = (
        "id",
        "title",
        "city",
        "supplier",
        "debt",
        "created_at",
    )
    list_filter = ("city",)
    list_display_links = ("supplier",)
    actions = (clear_debt,)
