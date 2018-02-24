from django.urls import path

from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('register', views.Register.as_view(), name='register'),
    path('photos/category/<str:category_name>',
         views.PicturesByCategory.as_view(), name='category'),
    path('photos/tag/<str:tag_name>', views.PicturesByTag.as_view(), name='tag'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('photo/<int:picture_id>',
         views.PictureDetail.as_view(), name='photo_detail')
]
