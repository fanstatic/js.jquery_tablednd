# -*- coding: utf-8 -*-

"""
Created on 2013-02-22
"""

import os

from setuptools import find_packages
from setuptools import setup

version = '0.4'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_tablednd', 'test_jquery_tablednd.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_tablednd',
    version=version,
    description="Fanstatic packaging of jQuery TableDND",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/js.jquery_tablednd',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_tablednd = js.jquery_tablednd:library',
            ],
        },
    )
