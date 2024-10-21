import logging
from django.shortcuts import render
from .models import Letting


# Configuration du logger
logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index page for lettings, displaying a list of all available lettings.
    """
    lettings_list = Letting.objects.all()
    logger.info(f"Index view called. Number of lettings retrieved: {lettings_list.count()}")
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting, displaying its title and address.

    Args:
        request: The HTTP request object.
        letting_id: The primary key of the letting to display.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
    except Letting.DoesNotExist:
        logger.error(f"Letting with ID {letting_id} does not exist.")
        return render(request, '404.html')

    return render(request, 'lettings/letting.html', context)
