#!/usr/bin/env python

from distutils.core import setup

setup(name='django-granular-permissions',
      version='0.3.1',
      description='Django granular (row-level) permissions that inject themselves in a non-invasive fashion (without modifying the Django code)',
      author='Bartosz Ptaszynski',
      author_email='yazzgoth@gmail.com',
      url='http://code.google.com/p/django-granular-permissions/',
      packages=['django_granular_permissions', 'django_granular_permissions.migrations'],
 )

