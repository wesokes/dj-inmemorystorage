# -*- coding: utf-8 -*-

from setuptools import setup

requires = ['Django>=1.9', 'six>=1.4.1']
tests_require = requires

setup(
    name="ambition-inmemorystorage",
    description="A non-persistent in-memory data storage backend for Django.",
    version="1.5.0",
    url="https://github.com/waveaccounting/dj-inmemorystorage",
    long_description=open('README.rst').read(),
    author='Cody Soyland, Seán Hayes, Tore Birkeland, Nick Presta',
    author_email='opensource@waveapps.com',
    packages=[
        'inmemorystorage',
    ],
    zip_safe=True,
    install_requires=requires,
    tests_require=tests_require,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Private :: Do Not Upload'
    ]
)
