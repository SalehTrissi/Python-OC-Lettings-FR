from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingsIntegrationTest(TestCase):

    def setUp(self):
        """
        Configure une adresse et une location de test pour l'intégration entre modèles, vues,
        et URLs.
        """
        self.address = Address.objects.create(
            number=150,
            street='Boulevard Macdonald',
            city='Paris',
            state='PA',
            zip_code=75019,
            country_iso_code='FR'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_index_view_integration(self):
        """
        Teste si la vue index intègre correctement les modèles Letting et Address
        et renvoie un statut 200.
        """
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Letting')

    def test_letting_view_integration(self):
        """
        Teste si la vue d'un letting spécifique intègre correctement le modèle Letting
        avec son adresse.
        """
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '150 Boulevard Macdonald')

    def test_address_and_letting_relationship(self):
        """
        Teste si une location (Letting) est correctement associée à une adresse (Address).
        """
        self.assertEqual(self.letting.address, self.address)
