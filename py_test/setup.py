# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='py_test',

    version='0.0.1',

    description='py test',

    url='',

    # Author details
    author='Test',
    author_email='test@',

    # Choose your license
    license='TEST',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Test Middleware',

        # Pick your license as you wish (should match "license" above)
        'License :: TEST',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    # What does your project relate to?
    keywords='Test middleware',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # test_suite='setup.test_suite',
    test_suite='test_suite_loader.test_suite',
    tests_require=[],
    install_requires=[
        'setuptools>=38.5.1'
    ],
)

