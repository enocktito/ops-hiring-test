import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as copy_right:
    LICENSE = copy_right.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='core',
    # ext_modules=cythonize(ext_modules),
    version='0.1.0',
    packages=['user'],
    include_package_data=True,
    license=LICENSE,
    description='unicore devops test',
    long_description=README,
    url='https://github.com/sphinxxanxus',
    author='Corentin All',
    author_email='corentinalcoy@gmail.com',
    install_requires=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0.6',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
