"""
URL configuration for the lettings application.

This module defines the URL patterns that map to the views in the
lettings app, using the app_name 'lettings' as a namespace.
"""
from django.urls import path
from . import views

# Defines the URL namespace for the lettings app
app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
