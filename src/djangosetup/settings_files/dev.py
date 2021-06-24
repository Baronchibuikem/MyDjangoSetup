from djangosetup.settings_files.common import *  # NOQA (ignore all errors on this line)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
