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
  license='GPLv3+',
  classifiers=(
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules'
  )
)
