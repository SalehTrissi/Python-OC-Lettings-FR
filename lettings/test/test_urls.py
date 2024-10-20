from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index, letting


class LettingsURLsTest(SimpleTestCase):

    def test_index_url_resolves(self):
        """
        Teste si l'URL de la page d'index des locations résout la bonne vue.
        """

        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        """
        Teste si l'URL d'une location spécifique résout la bonne vue.
        """
        url = reverse('lettings:letting', args=[1])
        self.assertEqual(resolve(url).func, letting)
