#!/usr/bin/env python

from setuptools import setup

setup(
    name='copytext',
    version='0.1.2',
    description='A library for accessing a spreadsheet as a native Python object suitable for templating.',
    long_description=open('README').read(),
    author='NPR Visuals Team',
    author_email='nprapps@npr.org',
    url='http://copytext.readthedocs.org/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['copytext'],
    install_requires = [
        'openpyxl>=1.8.5',
        'MarkupSafe>=0.21'
    ]
)
