from ._base import *

ALLOWED_HOSTS = ['*']


REST_FRAMEWORK = {
    'DEFAULT_PERMISSIONS_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
