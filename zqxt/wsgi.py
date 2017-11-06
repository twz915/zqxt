"""
WSGI config for zqxt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

os.environ["DJANGO_SETTINGS_MODULE"] = "zqxt.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
