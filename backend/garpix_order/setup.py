from setuptools import setup, find_packages
# from os import path
# from m2r import convert
# from django.conf import settings
#
#
# here = path.join(path.abspath(path.dirname(__file__)), 'garpix_order')
#
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='garpix_order',
    version='1.0.0-rc5',
    description='',
    long_description='',
    url='https://github.com/lilrazlil/test',
    author='Garpix LTD',
    author_email='info@garpix.com',
    license='MIT',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django >= 1.11',
        'djangorestframework >= 3.8',
        'django-fsm == 3.0.0',
    ],
)