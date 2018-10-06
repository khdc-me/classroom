from ._base import *

ALLOWED_HOSTS = ['*']


REST_FRAMEWORK = {
    'DEFAULT_PERMISSIONS_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

CORS_ORIGIN_WHITELIST = (
    'localost:3000/',
)
