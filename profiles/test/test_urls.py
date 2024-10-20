from django.urls import resolve, reverse
from django.test import SimpleTestCase
from profiles.views import index, profile


class ProfilesURLsTest(SimpleTestCase):

    def test_index_url_resolves(self):
        """
        Teste si l'URL de la page d'index des profils résout la bonne vue.
        """
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url_resolves(self):
        """
        Teste si l'URL d'un profil utilisateur spécifique résout la bonne vue.
        """
        url = reverse('profiles:profile', args=['Trissi'])
        self.assertEqual(resolve(url).func, profile)
