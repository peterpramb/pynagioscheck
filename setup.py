#!/usr/bin/env python

import sys

# Python version check
if sys.version_info < (2, 6) or \
        (sys.version_info >= (3,) and sys.version_info < (3, 4)):
    error = """
Pynagioscheck 0.1.7+ requires Python 2 >= 2.6, or Python 3 >= 3.4.
Older Python versions were supported up to pynagioscheck 0.1.6.

Python %s detected.

Please upgrade your Python version, or resort to pynagioscheck 0.1.6.

""" % '.'.join([str(v) for v in sys.version_info[:3]])

    sys.stderr.write(error)
    sys.exit(1)

# Supported version, continue
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from io import open
from os import path
from nagioscheck import __version__ as version

# Import README (the old way, for backward compatibility)
basedir = path.abspath(path.dirname(__file__))
f = open(path.join(basedir, 'README.rst'), 'r', encoding='utf-8')
try:
    long_description = f.read()
finally:
    f.close()

# Entry point
setup(
    name='nagioscheck',
    version=version,
    description='A Python framework for Nagios plugin developers',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/peterpramb/pynagioscheck',
    download_url='https://pypi.org/project/nagioscheck/',
    author='Saj Goonatilleke',
    author_email='sg@redu.cx',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Monitoring',
    ],
    keywords='Nagios Icinga plugin check monitoring',
    py_modules=['nagioscheck'],
    platforms=['Linux', 'Unix'],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    setup_requires=[
        'setuptools>=24.2.0',
    ],
    extras_require={
        'test': ['tox>=3.8.0'],
    },
    options={
        'bdist_wheel': {'universal': True},
        'metadata': {'license_files': 'LICENSE.txt'},
    },
)
