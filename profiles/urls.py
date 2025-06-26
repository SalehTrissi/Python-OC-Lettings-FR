"""
URL configuration for the profiles application.

This module defines the URL patterns that map to the views in the
profiles app, using the app_name 'profiles' as a namespace.
"""
from django.urls import path
from . import views

# Defines the URL namespace for the profiles app
app_name = 'profiles'

# Defines the URL patterns for the profiles app
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
