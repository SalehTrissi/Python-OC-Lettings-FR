from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesViewsTest(TestCase):

    def setUp(self):
        """
        Configure un utilisateur et un profil de test.
        """
        self.user = User.objects.create(
            username='Trissi'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_index_view_status_code(self):
        """
        Teste si la vue index des profils renvoie un statut 200 (succès).
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_contains_username(self):
        """
        Teste si la vue index contient le nom d'utilisateur du profil.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, 'Trissi')

    def test_profile_view_status_code(self):
        """
        Teste si la vue d'un profil utilisateur spécifique renvoie un statut 200 (succès).
        """
        response = self.client.get(reverse('profiles:profile', args=['Trissi']))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_contains_favorite_city(self):
        """
        Teste si la vue d'un profil utilisateur spécifique contient la ville favorite.
        """
        response = self.client.get(reverse('profiles:profile', args=['Trissi']))
        self.assertContains(response, 'Paris')

    def test_profile_view_nonexistent_user(self):
        """
        Teste le comportement de la vue profile lorsqu'un utilisateur inexistant est fourni.
        Devrait retourner une page 404.
        """
        response = self.client.get(reverse('profiles:profile', args=['nonexistent_user']))
        self.assertEqual(response.status_code, 404)