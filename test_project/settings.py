DEBUG = True

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'exchange'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db'
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

OPENEXCHANGERATES_API_KEY = '<DUMMY_KEY>'
