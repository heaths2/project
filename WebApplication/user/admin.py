from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'email', 'username', 'password', 'phone', 'department',
        'date_of_birth', 'gender', 'date_joined', 'last_login',
        'is_active', 'is_admin', 'is_staff', 'is_superuser',
    ]
    list_filter = ('id', 'email', 'username', 'password', 'phone', 'department',
        'date_of_birth', 'gender', 'date_joined', 'last_login',
        'is_active', 'is_admin', 'is_staff', 'is_superuser',)
    fieldsets = [
        ('계정', {'fields': ('email', 'username')}),
        ('개인 정보', {'fields': ('phone', 'date_of_birth', 'gender', 'department', 'date_joined', 'last_login')}),
        ('권한', {'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser')}),
    ]


admin.site.register(User)

