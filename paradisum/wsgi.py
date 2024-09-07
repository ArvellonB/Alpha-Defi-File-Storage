"""
WSGI config for paradisum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/var/www/paradisum/paradisum')

sys.path.append('/var/www/paradisum/paradisumenv/lib/python3.9/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paradisum.settings')

application = get_wsgi_application()
