"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import json
from pathlib import Path

config_path = Path(__file__).resolve().parent.parent
config_file = open(os.path.join(config_path, 'config.json'))
config_json = json.load(config_file)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config_json['ENV'])

application = get_wsgi_application()

app = application
