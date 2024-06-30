from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'surname', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name', 'surname')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'surname')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    readonly_fields = ('created_at', 'last_login', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)

