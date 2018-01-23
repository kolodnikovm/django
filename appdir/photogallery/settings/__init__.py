from os import environ

from split_settings.tools import include, optional

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # standard django settings
    'components/database.py',  # postgres

    # Select the right env:
    'environments/%s.py' % ENV,
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
