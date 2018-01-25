from django.contrib import admin

from .models import Category, Picture, Tag


class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['picture_name']
    list_filter = ('category',)



admin.site.register(Category)
admin.site.register(Picture, GalleryAdmin)
admin.site.register(Tag)
