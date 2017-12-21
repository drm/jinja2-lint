#!/usr/bin/env python

from distutils.core import setup

setup(
    name='j2lint',
    version='1.0',
    description='jinja2 linter',
    author='Gerard van Helden',
    license='DBAD',
    url='https://github.com/drm/jinja2-lint',
    entry_points={
        'console_scripts': [
            'j2lint=j2lint:main',
            'jinja2lint=j2lint:main',
        ]
    },
    packages=[
        'j2lint',
    ],
    install_requires=[
        'jinja2'
    ],
)
