from django.contrib import admin
from customers.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "city", "date_joined")
    search_fields = ("email", "phone", "city")
    ordering = ("-date_joined",)

