"""
ASGI config for ExploreTheWorld project.
This configuration exposes the ASGI callable as a module-level variable named 'application'.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeloco.settings')

application = get_asgi_application()