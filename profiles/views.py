import logging
from django.shortcuts import render
from .models import Profile


# Configuration du logger
logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the index page for profiles, displaying a list of all profiles.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'profiles/index.html' template with a list of profiles.
    """
    profiles_list = Profile.objects.all()
    logger.info(f"Index view called. Number of profiles retrieved: {profiles_list.count()}")
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders the detail page for a specific user profile.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile is being displayed.

    Returns:
        HttpResponse: The rendered 'profiles/profile.html' template with the profile details.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Profile view called for username: {username}")
        context = {'profile': profile}
    except Profile.DoesNotExist:
        logger.error(f"Profile for username {username} does not exist.")
        return render(request, '404.html')

    return render(request, 'profiles/profile.html', context)
