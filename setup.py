#!/usr/bin/env python
from setuptools import setup
from os.path import dirname, join

here = dirname(__file__)


setup(name='collector',
      version='1.0',
      description='Market making bot for BitMEX API',
      long_description_content_type='text/markdown',
      author='Samuel Reed',
      author_email='sam@bitmex.com',
      install_requires=[
          'requests',
          'websocket-client',
          'future'
      ],
      packages=['auth', 'utils'],
      )