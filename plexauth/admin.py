from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PlexUser
# Register your models here.

class PlexUserAdmin(UserAdmin):
    model = PlexUser

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