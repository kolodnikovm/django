from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ExternalUser

admin.site.register(ExternalUser, UserAdmin)
