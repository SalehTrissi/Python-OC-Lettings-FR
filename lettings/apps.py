"""
App configuration for the lettings application.

This file defines the configuration for the 'lettings' Django app,
setting its name.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
