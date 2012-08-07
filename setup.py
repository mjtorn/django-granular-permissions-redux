#!/usr/bin/env python

from distutils.core import setup

setup(name='django-granular-permissions',
      version='0.5',
      description='Django granular (row-level) permissions that inject themselves in a non-invasive fashion (without modifying the Django code)',
      author='Yazzgoth@googlecode, Ryates@github, Eternicode@bitbucket, mjtorn@github',
      author_email='yazzgoth@gmail.com',
      url='http://github.com/mjtorn/django-granular-permissions-redux/',
      packages=['django_granular_permissions'],
)

