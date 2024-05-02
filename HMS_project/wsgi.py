"""
WSGI config for HMS_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import sys
import os
from django.core.wsgi import get_wsgi_application


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HMS_project.settings')

application = get_wsgi_application()
print(sys.path)