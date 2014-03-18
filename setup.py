import os

from setuptools import setup, find_packages
import storages

SRC_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SRC_ROOT, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='django-storages',
    version=storages.__version__,
    packages=find_packages(),

    author='David Larlet',
    author_email='david@larlet.fr',
    license='BSD',
    description='Support for many storages (S3, MogileFS, etc) in Django.',
    url='http://code.welldev.org/django-storages/',
    install_requires=required,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite='tests.main',
    zip_safe=False,
)
