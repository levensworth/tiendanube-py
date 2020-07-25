import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='tiendanube',
    packages=[
        'tiendanube',
        'tiendanube.resources',
    ],
    version='1.1',
    description='',
    license='MIT',
    long_description=read('README.rst'),
    url='https://github.com/jobiols/tiendanube-py',
    download_url='https://github.com/jobiols/tiendanube-py/tarball/1.1',


    author='Jorge Obiols',
    author_email='jorge.obiols@gmail.com',

    install_requires=[
        "furl==2.1.0",
        "mock==3.0.5",
        "pytz==2020.1",
        "requests==2.24.0",
    ],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ),
)
