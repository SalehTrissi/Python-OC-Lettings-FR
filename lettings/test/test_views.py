from django.test import TestCase
from lettings.models import Address, Letting
from django.urls import reverse


class LettingsViewsTest(TestCase):

    def setUp(self):
        """
        Configure un contexte de test avec un exemple de location et d'adresse.
        """
        self.address = Address.objects.create(
            number=150,
            street='Boulverad MAcdonald',
            city='Paris',
            state='PA',
            zip_code=75019,
            country_iso_code='FR'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_index_view_status_code(self):
        """
        Teste si la vue index renvoie un statut 200 (succès).
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_contains_letting(self):
        """
        Teste si la vue index contient le titre de la location.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, 'Test Letting')

    def test_letting_view_status_code(self):
        """
        Teste si la vue d'une location spécifique renvoie un statut 200 (succès).
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)

    def test_letting_view_contains_address(self):
        """
        Teste si la vue d'une location spécifique contient l'adresse associée.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertContains(response, '150 Boulverad MAcdonald')
        self.assertContains(response, 'Paris, PA 75019')
        self.assertContains(response, 'FR')
