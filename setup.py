#!/usr/bin/env python3
from setuptools import setup

setup(name='my_hello_vitoria', version='0.1', packages=['my_hello'], author='Vitoria Helena', classifiers=[
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ], install_requires=['pytest'], scripts=['scripts/hello.py'])