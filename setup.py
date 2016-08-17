""" setup.py - Script to install package using distutils

For help options run:
$ python setup.py --help

"""
# Author: elchinot7

from setuptools import setup
from streemapy import streema

VERSION = streema.__version__

setup_args = dict(name='streemapy',
                  version=VERSION,
                  author='elchinot7',
                  author_email='efraazul@gmail.com',
                  url='https://github.com/elchinot7/streema.py',
                  packages=['streemapy'],
                  scripts=['streemapy/streema.py'],
                  package_data={},
                  license="Modified BSD license",
                  description="""streemapy extracts info from streema.com""",
                  long_description=open('README.rst').read(),
                  classifiers=["Topic :: Utilities",
                               "Intended Audience :: Music/tools",
                               "License :: OSI Approved :: BSD License",
                               "Operating System :: OS Independent",
                               "Programming Language :: Python",
                               "Programming Language :: Python :: 2.7",
                               "Programming Language :: Python :: 3.4",
                               ],
                  install_requires=[],
                  )

if __name__ == "__main__":
    setup(**setup_args)
