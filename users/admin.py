from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "username",
                    "name",
                    "email",
                    "password",
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Importand Dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "name",
        "is_host",
    )
