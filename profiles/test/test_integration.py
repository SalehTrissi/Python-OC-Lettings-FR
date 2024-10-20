from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfilesIntegrationTest(TestCase):

    def setUp(self):
        """
        Configure un utilisateur et un profil de test pour l'intégration entre modèles, vues,
        et URLs.
        """
        self.user = User.objects.create(
            username='Trissi'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_index_view_integration(self):
        """
        Teste si la vue index intègre correctement les modèles User et Profile
        et renvoie un statut 200.
        """
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trissi')

    def test_profile_view_integration(self):
        """
        Teste si la vue d'un profil spécifique intègre correctement les données du modèle Profile.
        """
        url = reverse('profiles:profile', args=[self.user])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trissi')
        self.assertContains(response, 'Paris')

    def test_user_and_profile_relationship(self):
        """
        Teste si un profil (Profile) est correctement associé à un utilisateur (User).
        """
        self.assertEqual(self.profile.user, self.user)
