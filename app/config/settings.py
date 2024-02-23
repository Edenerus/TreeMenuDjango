import os
from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',

                 ]

INTERNAL_IPS = ["127.0.0.1",
                "localhost",

                ]

CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:8000",

                        ]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

include(
    'components/apps.py',
    'components/database.py',
    'components/internationalization.py',
    'components/middleware.py',
    'components/templates.py',
    'components/validators.py',
    'components/logging.py',

)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
