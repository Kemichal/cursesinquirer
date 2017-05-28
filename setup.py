# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from cursesinquirer import __version__

setup(
    name='cursesinquirer',
    packages=find_packages(exclude="examples"),
    version=__version__,
    description='A library to create curses based CLIs',
    long_description='A library to create curses based CLIs',
    author='Robert Andersson',
    author_email='kemichal@gmail.com',
    license='MIT',
    url='https://github.com/kemichal/cursesinquirer',
    keywords=['curses', 'inquirer', 'questionnaire', 'cli', 'terminal', 'development'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)
