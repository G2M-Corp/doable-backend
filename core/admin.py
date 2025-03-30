"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from core.models import User, Categoria, Tarefa


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name", "imagem_preview"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "passage_id", "imagem")}),
        (
            _( "Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "imagem",
                ),
            },
        ),
    )
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.imagem.url)
        return "-"
    imagem_preview.short_description = "Imagem"


admin.site.register(User, UserAdmin)
admin.site.register(Categoria)
admin.site.register(Tarefa)
