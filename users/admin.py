from django.contrib import admin

from users.models import User


@admin.register(User)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("id", "email",)
