from django.contrib import admin
from .models import Letting
from .models import Address


# Register Letting and Address models in the Django admin interface.
admin.site.register(Letting)
admin.site.register(Address)
