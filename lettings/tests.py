import pytest
from django.urls import reverse
from django.test import Client
from .models import Letting, Address


@pytest.mark.django_db
def test_letting_model():
    """
    Tests the Letting and Address model creation and string representation.
    """
    address = Address.objects.create(
        number=123,
        street='Main St',
        city='Springfield',
        state='IL',
        zip_code=62701,
        country_iso_code='USA'
    )
    letting = Letting.objects.create(
        title='Cozy Apartment',
        address=address
    )
    assert str(letting) == 'Cozy Apartment'
    assert str(address) == '123 Main St'
    assert letting.address.city == 'Springfield'


@pytest.mark.django_db
def test_letting_index_view():
    """
    Tests the lettings index view to ensure it loads correctly
    and displays a letting's title.
    """
    client = Client()
    address = Address.objects.create(
        number=1, street="Main St", city="Anytown", state="AN",
        zip_code=12345, country_iso_code="USA")
    Letting.objects.create(title="Cozy Cottage", address=address)

    path = reverse('lettings:index')
    response = client.get(path)

    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content
    assert b"Cozy Cottage" in response.content


@pytest.mark.django_db
def test_letting_detail_view():
    """
    Tests the letting detail view to ensure it loads correctly
    and displays the letting's information.
    """
    client = Client()
    address = Address.objects.create(
        number=2, street="Oak Ave", city="Someplace", state="SP",
        zip_code=54321, country_iso_code="USA")
    letting = Letting.objects.create(title="Spacious Loft", address=address)

    path = reverse('lettings:letting', kwargs={'letting_id': letting.pk})
    response = client.get(path)

    assert response.status_code == 200
    assert b"<title>Spacious Loft</title>" in response.content
    assert b"Oak Ave" in response.content
