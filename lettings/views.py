from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders the index page for lettings, displaying a list of all available lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting, displaying its title and address.

    Args:
        request: The HTTP request object.
        letting_id: The primary key of the letting to display.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
