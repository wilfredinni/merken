import os
from .settings.base import STATIC_ROOT
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
