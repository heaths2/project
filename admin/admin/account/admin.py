from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User

admin.site.register(User)
