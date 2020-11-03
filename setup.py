import os
from setuptools import find_packages, setup

# from Cython.Build import cythonize

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as copy_right:
    LICENSE = copy_right.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

ext_modules = [
    # core
    'core/*.py',

    # core/abstract
    'core/abstract/*.py',
    'core/abstract/models/*.py',
    'core/abstract/serializers/*.py',
    'core/abstract/viewsets/*.py',

    # core/auth
    'core/auth/*.py',
    'core/auth/models/*.py',
    'core/auth/viewsets/*.py',
    'core/auth/authentications/*.py',

    # core/menu
    'core/menu/models/*.py',
    'core/menu/*.py',
    'core/menu/viewsets/*.py',

    # core/restaurant
    'core/restaurant/*.py',
    'core/restaurant/models/*.py',
    'core/restaurant/serializers/*.py',
    'core/restaurant/viewsets/*.py',

    # core/category
    'core/category/*.py',
    'core/category/models/*.py',
    'core/category/serializers/*.py',
    'core/category/viewsets/*.py',

    # core/user
    'core/user/models/*.py',
    'core/user/*.py',

    # core/garnish
    'core/garnish/*.py',

    # core/drink
    'core/drink/*.py',
    'core/drink/viewsets/*.py',

    # core/websocket
    'core/websocket/*.py',
    'core/websocket/serializers/*.py',
    'core/websocket/models/*.py',
    'core/websocket/consumers/*.py',

    # core/order
    'core/order/*.py',
    'core/order/models/*.py',
    'core/order/serializers/*.py',
    'core/order/crons/*py',

    # core/xlib
    'core/xlib/*.py',
    'core/xlib/rest/*.py',
    'core/xlib/testcases/*.py',

    # core/account
    'core/account/*.py',
    'core/account/viewsets/*.py',

    'core/account/consumer/*.py',
    'core/account/consumer/models/*.py',
    'core/account/consumer/serializers/*.py',

    'core/account/delivery/*.py',
    'core/account/delivery/models/*.py',
    'core/account/delivery/serializers/*.py',

    'core/account/proprietor/*.py',

    'core/currency/*.py',
    'core/proxies/*.py',
    'core/proxies/google/*.py',
    'core/proxies/google/*.py',
    'core/proxies/google/maps/*.py',
]

setup(
    name='core',
    # ext_modules=cythonize(ext_modules),
    version='0.1.0',
    packages=[f'core.{p}' for p in find_packages('core')],
    include_package_data=True,
    license=LICENSE,
    description='unicore core apps',
    long_description=README,
    url='https://github.com/sphinxxanxus',
    author='Corentin Allohoumbo',
    author_email='corentinalcoy@gmail.com',
    install_requires=[
        'Django==3.1.2',
        'djangorestframework==3.12.1',
        'drf-nested-routers==0.92.1',
        'psycopg2-binary==2.8.6',
        'Pillow==8.0.1',
        'PyJWT==1.7.1',
        'requests==2.24.0',
        'dj-database-url==0.5.0',
        "boto3==1.16.9",
        "django-storages==1.10.1",
        "channels==2.4.0",
        "channels-redis==3.2.0",
        "celery==4.4.6",
        "redis==3.5.3",
        "flower==0.9.5",
        "googlemaps==4.4.2",
        "django-redis==4.12.1",
        # "Cython==0.29.21",
        'sentry-sdk==0.19.1',
        "twilio==6.46.0",
        'libgravatar==0.2.4',
        'onesignal-sdk==2.0.0',
        "slackclient==2.8.2",
        "aiocontextvars==0.2.2",
        "requests-unixsocket==0.2.0",
        "django-cors-headers==3.5.0",
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
