from django.shortcuts import render


def index(request):
    """
    Renders the home page of the 'oc_lettings_site'.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'index.html' template.
    """
    return render(request, 'index.html')
