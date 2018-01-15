from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Picture, Tag

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(Tag)