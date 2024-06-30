from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Profile


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


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image', 'bio')
    search_fields = ('user__email', 'user__name', 'user__surname')
    list_filter = ('user__is_active',)
    readonly_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        (_('Profile Details'), {
            'fields': ('profile_image', 'bio')
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Profile, ProfileAdmin)