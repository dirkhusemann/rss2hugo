#!/usr/bin/env python3.9
from setuptools import setup

setup(
    name='rss2hugo',
    version='1.0.0',
    packages=['rss2hugo'],
    package_dir={'': 'src'},
    url='',
    license='GPL-2',
    author='Dirk Husemann',
    author_email='dirk@d2h.net',
    description='Converts RSS feed to hugo articles',
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'rss2hugo = rss2hugo.rss2hugo:cli',
        ],
    },
)
