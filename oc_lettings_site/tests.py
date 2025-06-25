import pytest
from django.test import Client
from django.http import HttpRequest
from oc_lettings_site.views import handler500


@pytest.mark.django_db
def test_404_page_template_and_content(client: Client):
    """
    Tests that a request to a non-existent URL returns the custom 404 page
    with the correct status code and content.
    """
    response = client.get('/this-url-does-not-exist/')

    assert response.status_code == 404
    assert '404.html' in [t.name for t in response.templates]
    assert b'<h1 class="display-1 text-primary">404</h1>' in response.content
    assert b'<h2 class="mb-4">Page Not Found</h2>' in response.content


@pytest.mark.django_db
def test_500_handler_directly():
    """
    Tests the 500 handler directly by calling the view function.
    This is a more direct approach that avoids URL routing complexities.
    """
    # Create a dummy request object
    request = HttpRequest()
    request.method = 'GET'

    # Call the handler function directly
    response = handler500(request)

    # Check the response
    assert response.status_code == 500
    assert b'<h1 class="display-1 text-primary">500</h1>' in response.content
    assert b'<h2 class="mb-4">Internal Server Error</h2>' in response.content
    assert b"We're sorry, something went wrong on our end" in response.content
