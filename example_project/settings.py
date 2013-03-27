DEBUG = True
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}
INSTALLED_APPS=(
    'south',
    'feedback',
    'django_nose',
)
SITE_ID=1
ROOT_URLCONF = 'feedback.urls'
SECRET_KEY='this-is-just-for-tests-so-not-that-secret'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
