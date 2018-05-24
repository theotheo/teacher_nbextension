# from nbsetuptools import setup
from setuptools import setup
from os.path import abspath, dirname, join

NAME = 'teacher_nbextension'
AUTHOR = 'i'
EMAIL = 'ibelyalov@yandex.ru'
DESCRIPTION = 'Teacher extension for Jupyter'

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    email=EMAIL,
    version="0.1.0",
    static=join(abspath(dirname(__file__)), 'static'),
    install_requires=[
        'python-logstash'
    ],
    include_package_data=True
)
