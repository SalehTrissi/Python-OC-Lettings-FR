from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile with a one-to-one relationship to the User model.
    Includes additional information such as the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the username of the associated user.
        """
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
