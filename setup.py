#!/usr/bin/env python
# encoding: utf-8

"""Packaging script."""

import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, 'README.rst')).read()

setup(
    name="c2chth",
    version="0.1.0",
    author="tlueckow",
    description='Code to Code transformation. Apply a pattern to a list of similar shaped code blocks. Hope This Helps.',
    license="MIT",
    keywords="sed python transformation",
    url="http://github.com/tlueckow/code2code-hth",
    py_modules=['c2chth'],
    entry_points={'console_scripts': ['c2chth=c2chth:main']},
    long_description=readme,
    test_suite='tests',
    setup_requires=[],
    tests_require=['mock'],
    classifiers=["Development Status :: 5 - Production/Stable",
                 "License :: OSI Approved :: MIT License",
                 "Environment :: Console",
                 "Natural Language :: English",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Topic :: Software Development",
                 "Topic :: Software Development :: Code Generators",
                 "Topic :: Text Editors :: Text Processing",
                 "Topic :: Text Processing :: Filters",
                 "Topic :: Utilities",
                 "Intended Audience :: Developers",
                ],
)
