from django.test import TestCase
from lettings.models import Address, Letting


class LettingModelTest(TestCase):

    def setUp(self):
        """
        Sets up the initial test data.
        This method is called before each test to create instances of Address and Letting.
        """
        self.address = Address.objects.create(
            number=150,
            street='BD Macdonald',
            city='Paris',
            state='Pr',
            zip_code=75019,
            country_iso_code='FR'
        )

        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_letting_str(self):
        """
        Tests the string representation of the Letting instance.
        Asserts that the __str__ method of Letting returns the correct title.
        """
        self.assertEqual(str(self.letting), 'Test Letting')

    def test_address_str(self):
        """
        Tests the string representation of the Address instance.
        Asserts that the __str__ method of Address returns the correct address format.
        """
        self.assertEqual(str(self.address), '150 BD Macdonald')
