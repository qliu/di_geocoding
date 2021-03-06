"""
WSGI config for geocodingtool project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/django-apps/di_geocoding/geocodingtool/')
# Use this for single Django site in a single mod_wsgi process
#os.environ.setdefault("PYTHON_EGG_CACHE", "/django-apps/di_geocoding/geocodingtool/egg_cache")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geocodingtool.settings")
# Use this for multiple Django site in a single mod_wsgi process
os.environ["PYTHON_EGG_CACHE"] = "/django-apps/di_geocoding/geocodingtool/egg_cache"
os.environ["DJANGO_SETTINGS_MODULE"] = "geocodingtool.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()