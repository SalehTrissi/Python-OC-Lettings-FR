"""
Defines the views for the lettings application.

This module contains the logic for rendering the lettings index
and detail pages.
"""
from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Displays a list of all available lettings.

    Args:
        request: The HTTP request object.

    Returns:
        An HttpResponse object rendering the lettings index page.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Displays the details page for a specific letting.

    Args:
        request: The HTTP request object.
        letting_id (int): The primary key of the letting to display.

    Returns:
        An HttpResponse object rendering the individual letting page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
