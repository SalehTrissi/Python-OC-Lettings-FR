"""
Configuration for the lettings app in the Django admin interface.

This file registers the Letting and Address models to make them
manageable through the admin site.
"""
from django.contrib import admin
from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
