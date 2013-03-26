#!/usr/bin/env python
import sys

from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite',
            }
        },
        INSTALLED_APPS=(
            'feedback',
            'django_nose',
        ),
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
        TEST_RUNNER = 'django_nose.NoseTestSuiteRunner',
        NOSE_ARGS = ['--with-coverage','--cover-package=feedback']
    )


from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['feedback.tests', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()

