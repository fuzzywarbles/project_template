# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='project_template',
    version='0.1.0',
    description='project_template',
    long_description=readme,
    author='Chris Kendzora',
    author_email='me@kennethreitz.com',
    url='https://github.com/fuzzywarbles/project_template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

