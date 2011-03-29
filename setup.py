#!/usr/bin/env python
import os,sys
from setuptools import setup, find_packages

version = "0.1.0"

long_description = open('README.rst').read()

setup(name='django-flatpages-tinymce',
      version=version,
      description="HTML editor on django.contrib.flatpages",
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Natural Language :: Russian',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
      ],
      keywords='flatpages tinymce WYSIWYG',
      author='McLaud Jr',
      author_email='mjr@itage.biz',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      requires = ['django_tinymce (>=1.5)', 'Django (>=1.3)'],
      entry_points={},
      zip_safe=False)
