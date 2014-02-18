#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import bottle

setup(name='Bottle-Async',
      version=bottle.__version__,
      description='A fork of Bottle to add support for asyncio.',
      long_description=bottle.__doc__,
      author=bottle.__author__ + ", Don Brown",
      author_email='mrdon@twdata.org',
      url='https://github.com/mrdon/bottle',
      py_modules=['bottle'],
      scripts=['bottle.py'],
      license='MIT',
      install_requires=[
        'aiohttp>=0.6'
      ],
      platforms = 'any',
      classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        ],
     )



