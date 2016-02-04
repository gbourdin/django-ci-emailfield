from django.conf import settings


def pytest_configure():
    settings.configure(
        MIDDLEWARE_CLASSES=[],
        CACHES={},
        INSTALLED_APPS=['tests.app'],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite',
            },
            'psql': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'django_ciemailfield',
            },
        }
    )

    from django import setup
    setup()
