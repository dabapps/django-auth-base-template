import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'auth_base_template',
)

LOGGED_IN_BASE_TEMPLATE = 'logged_in_base.html'
LOGGED_OUT_BASE_TEMPLATE = 'logged_out_base.html'
