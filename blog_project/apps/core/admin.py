from django.contrib import admin
from .models import Contact, AboutUs

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'resolved', 'resolved_by')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at', 'resolved')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message', 'resolved', 'resolved_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated_by', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'last_updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
