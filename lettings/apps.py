from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings app.
    Sets the default primary key field type and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
