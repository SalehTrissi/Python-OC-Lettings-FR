"""
App configuration for the profiles application.

This file defines the configuration for the 'profiles' Django app,
setting its name.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
