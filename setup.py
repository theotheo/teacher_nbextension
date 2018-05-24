# from nbsetuptools import setup
from setuptools import setup
from os.path import abspath, dirname, join

name = "teacher_nbextension"

setup(
    name=name,
    version="0.1.0",
    static=join(abspath(dirname(__file__)), 'static'),
    # packages=['.'],
    install_requires=[
        'python-logstash'
    ]
)
