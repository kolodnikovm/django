from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Picture, Tag

class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['picture_name']
    list_filter = ('category',)

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Picture, GalleryAdmin)
admin.site.register(Tag)