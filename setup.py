import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-plexauth',
    version='0.1.1',
    packages=['plexauth'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A django auth backend for authenticating against plex.tv',
    long_description=README,
    url='https://github.com/munnerz/django-plexauth',
    author='James Munnelly',
    author_email='james@munnelly.eu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'requests',
        'django-bootstrap3',
        'django-activelink',
    # more dependencies
    ],
)