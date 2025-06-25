from django.shortcuts import render


def index(request):
    """
    Renders and displays the main index page of the website.
    """
    return render(request, 'index.html')
