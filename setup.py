#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from glob import glob

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
        'biopython',
        'numpy',
        'matplotlib',
]

test_requirements = [
    'pytest',
    'pycmd',
]

setup(
    name='Wub',
    version='0.1.0',
    description="Tools and software components developed by the ONT Applications group.",
    long_description=readme,
    author="ONT Applications Group",
    author_email='Apps@nanoporetech.com',
    url='',
    packages=find_packages(exclude=["scripts"]),
    package_dir={'wub':
                 'wub'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='wub',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=test_requirements,
    scripts=[x for x in glob('scripts/*.py') if x != 'scripts/__init__.py']
)