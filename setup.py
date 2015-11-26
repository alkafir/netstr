#!/usr/bin/env python3

from distutils.core import setup
import netstring

setup(
  name='netstring',
  description='Netstrings module for Python 3',
  author='Alfredo Mungo',
  author_email='alfredo.mungo@openmailbox.org',
  url='https://github.com/alkafir/netstring',
  version=netstring.__version__,
  py_modules=('netstring',)
)
