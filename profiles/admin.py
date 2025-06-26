"""
Configuration for the profiles app in the Django admin interface.

This file registers the Profile model to make user profiles
manageable through the admin site.
"""
from django.contrib import admin
from .models import Profile


admin.site.register(Profile)
