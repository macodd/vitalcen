from pathlib import Path

import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': [BASE_DIR / 'db.sqlite3'],
    }
}

# set up for heroku's db
db_from_env = dj_database_url.config()

DATABASES['default'].update(db_from_env)

DATABASES['default']['CONN_MAX_AGE'] = 500

# hosts urls
ALLOWED_HOSTS = [
    'vitalcen.herokuapp.com',
    '.vitalcen.com',
]

# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True
SECURE_HSTS_PRELOAD = True
