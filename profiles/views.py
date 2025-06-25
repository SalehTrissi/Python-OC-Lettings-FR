from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Displays a list of all user profiles.

    Args:
        request: The HTTP request object.

    Returns:
        An HttpResponse object rendering the profiles index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Displays the details page for a specific profile.

    Args:
        request: The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        An HttpResponse object rendering the individual profile page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
