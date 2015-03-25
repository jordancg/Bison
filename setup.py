"""Bison - Site generator and deployment.

Copyright (C) 2015  Jordan Yerandi Cortes Guzman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

VERSION = '0.1.0'
SKELETON_FOLDERS = ['pages', 'static/css', 'static/images', \
'static/js', 'static/files', 'templates']

setup(name='Bison', \
    version=VERSION, \
    description='Site generator.', \
    long_description=open('README.md').read(), \
    url='http://github.com/jordancg/bison', \
    download_url='https://github.com/jordancg/bison/archive/master.zip', \
    author='Jordan Yerandi Cortes Guzman', \
    author_email='jordan.cortes@oracle.com', \
    license='GPL', \
    packages=['bison', 'bison.libs'], \
    entry_points={
        'console_scripts': [
            'bison = bison.cli:main',
        ],
    }, \
    zip_safe=False)
