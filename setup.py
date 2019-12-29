#!/usr/bin/env python

from setuptools import setup
from os import path
from io import open
from nagioscheck import __version__ as version

basedir = path.abspath(path.dirname(__file__))
with open(path.join(basedir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

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
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    setup_requires=[
        'setuptools>=28.8.0',
    ],
    extras_require={
        'test': ['tox>=3.8.0'],
    },
    options={
        'bdist_wheel': {'universal': True},
        'metadata': {'license_files': 'LICENSE.txt'},
    },
)
