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

from bison.libs.common import Common

F_CONFIG = "config.json"

def main():
    """d"""
    config = Common.open_file(F_CONFIG)

    # Delete the complete .build folder
    Common.clean_build(config['p_build'])

    # Create main folders
    Common.make_dir(config['p_build'])
    for language in config['languages']:
        Common.make_dir(config['p_build'] + language)

if __name__ == "__main__":
    main()
