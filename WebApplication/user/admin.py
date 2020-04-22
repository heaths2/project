from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'email', 'username', 'password', 'mobile_number',
        'date_of_birth', 'gender', 'date_joined', 'last_login',
        'is_active', 'is_admin', 'is_staff', 'is_superuser',
    ]


admin.site.register(User, UserModelAdmin)

