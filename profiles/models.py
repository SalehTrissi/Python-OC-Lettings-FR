from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extends the User model with a one-to-one link to store extra data."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Returns the username for display purposes."""
        return self.user.username
