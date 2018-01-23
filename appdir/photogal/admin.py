from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Picture, Tag, User


class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['picture_name']
    list_filter = ('category',)


class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['picture_name']
    list_filter = ('category',)

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Picture, GalleryAdmin)
admin.site.register(Tag)
