from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile


def index(request):
    """
    Renders and displays the main index page of the website.
    """
    lettings_list = Letting.objects.all()
    profiles_list = Profile.objects.all()

    # This line is intentionally causing a ZeroDivisionError for testing purposes. Error 500
    # test_erreur = 1 / 0

    context = {'lettings_list': lettings_list, 'profiles_list': profiles_list}
    return render(request, 'index.html', context)


def handler404(request, exception):
    """
    Custom view for 404 Page Not Found errors.
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Custom view for 500 Internal Server Error.
    """
    return render(request, '500.html', status=500)
