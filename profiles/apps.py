from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the 'profiles' application.
    Sets the default primary key field type and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
