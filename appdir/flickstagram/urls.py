from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('success_reg/', views.success_reg, name='success_reg'),
]