#!/usr/bin/env python3

from setuptools import setup
from smart_progress import __version__, __author__, __email__
from pathlib import Path

here = Path(__file__).parent

with (here / 'README.rst').open() as f:
	long_description = f.read()

setup(
	name='smart-progress',
	
	version=__version__,
	
	description='Smart progressbar with multiple backends selected depending on the environment',
	long_description=long_description,
	
	url='https://github.com/flying-sheep/smart-progress',
	
	author=__author__,
	author_email=__email__,
	
	license='GPLv3',
	
	classifiers=[
		'Development Status :: 4 - Beta',
		
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		
		'Environment :: Console',
		'Environment :: Web Environment',
		
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		
		'Topic :: Software Development :: Widget Sets',
		'Topic :: Utilities',
	],
	
	keywords='progress progressbar ipython jupyter console',
	
	py_modules=['smart_progress'],
	
	install_requires=['click'],
	extras_require={
		'ipynb': ['ipywidgets'],
	},
)