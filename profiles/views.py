from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Renders the index page for profiles, displaying a list of all profiles.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'profiles/index.html' template with a list of profiles.
    """
    profiles_list = Profile.objects.all()
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
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
