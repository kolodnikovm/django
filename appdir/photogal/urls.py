from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('photos', views.photos, name='photos'),
    path('<str:category_name>', views.category, name='category')
]