#!/usr/bin/env python

from setuptools import setup

setup(
    name='copytext',
    version='0.2.1',
    description='A library for accessing a spreadsheet as a native Python object suitable for templating.',
    long_description=open('README.md').read(),
    author='NPR Visuals Team',
    author_email='nprapps@npr.org',
    url='http://copytext.readthedocs.org/',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['copytext'],
    install_requires=[
        'openpyxl>=2.1.4',
        'six>=1.10.0'
    ],
    extras_require={
        'dev': [
            'Sphinx==1.5.6',
            'nose==1.1.2',
            'unittest2==0.5.1',
            'coverage==3.7.1',
            'flake8==3.5.0',
            'tox==3.0.0'
        ]
    }
)
