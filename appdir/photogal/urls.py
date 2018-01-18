from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.register, name='register'),
    path('photos/category/<str:category_name>', views.category_view, name='category'),
    path('photos/tag/<str:tag_name>', views.tag_view, name='tag'),
    path('upload', views.upload_view, name='upload'),
    path('photo/<int:pic_id>', views.photo_info_view, name='photo_info')
]