"""Run "python setup.py install" to install scandir."""

from setuptools import setup, Extension, find_packages
import os
import re

# Get version without importing scandir because that will lock the
# .pyd file (if scandir is already installed) so it can't be
# overwritten during the install process
with open(os.path.join(os.path.dirname(__file__), 'scandir/__init__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            _locals = {}
            exec(line, None, _locals)
            version = _locals['__version__']
            break
    else:
        raise Exception("Couldn't find version in setup.py")

setup(
    name='scandir',
    version=version,
    author='Ben Hoyt',
    author_email='benhoyt@gmail.com',
    url='https://github.com/benhoyt/scandir',
    license='New BSD License',
    description='scandir, a better directory iterator and faster os.walk()',
    long_description="scandir() is a generator version of os.listdir() that returns an "
                     "iterator over files in a directory, and also exposes the extra "
                     "information most OSes provide while iterating files in a directory "
                     "(such as type and stat information).\n"
                     "\n"
                     "This module also includes a version of os.walk() that uses scandir() "
                     "to speed it up significantly.\n"
                     "\n"
                     "NOTE: If you're using Python version 3.5+, os.scandir() and the speed "
                     "improvements to os.walk() are already available in the standard library.",
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    ext_modules=[Extension('scandir._scandir', ['scandir/_scandir.c'])],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
