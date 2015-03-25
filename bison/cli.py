#!/usr/bin/env python
# encoding: utf-8
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
import os
import argparse

def create(path):
    "Create a new project at the given path"

    if path is None:
        print os.getcwd()
    else:
        print path

def main():
    """A"""
    parser = argparse.ArgumentParser(description='A site preprocessor based \
        on Jinja2, a templating engine for Python')
    subparsers = parser.add_subparsers(description='The following options \
        are available:')

    # 'create' command
    parser_create = subparsers.add_parser('create', help='Create a new \
        project')
    parser_create.add_argument('--path', help='The path where the project \
        will be created')
    parser_create.set_defaults(target=create)

    args = parser.parse_args()

    arg_values = {key : value for key, value in vars(args).items() \
    if key != 'target'}

    args.target(**arg_values)

if __name__ == '__main__':
    main()
