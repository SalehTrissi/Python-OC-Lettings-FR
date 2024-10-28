from django.test import TestCase
from django.urls import reverse


class SiteIndexViewTest(TestCase):
    def test_index_view_status_code(self):
        """
        Test that the main site index view returns a status code 200.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_content(self):
        """
        Test that the main index view contains the welcome message.
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Welcome to Holiday Homes')
