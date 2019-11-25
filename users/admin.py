from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as djangoAdmin
from .models import User


class UserAdmin(djangoAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email')}),)


admin.site.register(User, UserAdmin)
