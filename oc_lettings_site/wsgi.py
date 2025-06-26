import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application


load_dotenv()  # Load environment variables from .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
