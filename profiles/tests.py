# profiles/tests.py
import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import Profile


@pytest.mark.django_db
def test_profile_model():
    """
    Tests the Profile model creation and string representation.
    """
    user = User.objects.create_user(username='testuser', password='password123')
    profile = Profile.objects.create(user=user, favorite_city="Dreamland")

    assert str(profile) == "testuser"
    assert profile.favorite_city == "Dreamland"


@pytest.mark.django_db
def test_profiles_index_view():
    """
    Tests the profiles index view to ensure it loads correctly
    and displays a user's profile.
    """
    client = Client()
    user = User.objects.create_user(username='janedoe', password='password123')
    Profile.objects.create(user=user, favorite_city="Metropolis")

    path = reverse('profiles:index')
    response = client.get(path)

    assert response.status_code == 200
    assert b"<title>Profiles</title>" in response.content
    assert b"janedoe" in response.content


@pytest.mark.django_db
def test_profile_detail_view():
    """
    Tests the profile detail view to ensure it loads correctly
    and displays the profile's information.
    """
    client = Client()
    user = User.objects.create_user(username='johndoe', password='password123')
    Profile.objects.create(user=user, favorite_city="Gotham")

    path = reverse('profiles:profile', kwargs={'username': 'johndoe'})
    response = client.get(path)

    assert response.status_code == 200
    assert b"<title>johndoe</title>" in response.content
    assert b"Favorite city :" in response.content
    assert b"Gotham" in response.content
