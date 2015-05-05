from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PlexUser
# Register your models here.

class PlexUserAdmin(UserAdmin):
    model = PlexUser
    filter_horizontal = []
    list_filter = []
    list_display = ('username', 'is_admin')
    fieldsets = (
        (None, {
            'fields': ('username', 'token')
        }),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_admin')
        }),
    )

admin.site.register(PlexUser, PlexUserAdmin)