from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfilModelTesst(TestCase):

    def setUp(self):
        """
        Sets up the initial test data.
        This method is called before each test to create a User and Profile instance.
        """
        self.user = User.objects.create(
            username='Trissi'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_profile_str(self):
        """
        Tests the string representation of the Profile instance.
        Asserts that the __str__ method of Profile returns the username of the associated user.
        """
        self.assertEqual(str(self.profile), 'Trissi')
