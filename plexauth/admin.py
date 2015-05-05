from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PlexUser
# Register your models here.

class PlexUserAdmin(UserAdmin):
    model = PlexUser

    fieldsets = UserAdmin.fieldsets
    fieldsets[0][1]['fields'] += ('token', )

admin.site.register(PlexUser, PlexUserAdmin)