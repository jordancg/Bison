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

This script grab the necessary information and create all the pages
that are ment to be part of the website
"""

import jinja2
import logging
from bison.libs.common import Common

F_INFO = "info.json"
F_CONFIG = "config.json"

def load_jinja2_env(template_folder):
    """Load the environment for the jinja2 template system"""
    return jinja2.Environment(loader=jinja2.FileSystemLoader(template_folder))

def main():
    """Main method that runs the build"""
    data = Common.open_file(F_INFO)
    config = Common.open_file(F_CONFIG)
    file_full_path = ""

    env = load_jinja2_env(config['p_template'])

    for index, page in data.iteritems():
        logging.info('Creating ' + index + ' page:')

        template = env.get_template(page['f_template'] + \
            config['f_template_ext'])

        for lang, content in page['content'].items():
            if lang == "NaL":
                if page['f_directory'] != '':
                    Common.make_dir(config['p_build'] + page['f_directory'])

                file_full_path = config['p_build'] + page['f_directory'] + \
                    page['f_name'] +page['f_endtype']
            else:
                if page['f_directory'] != '':
                    Common.make_dir(config['p_build'] + lang + '/' + \
                        page['f_directory'])

                file_full_path = config['p_build'] + lang + '/' + \
                    page['f_directory'] + page['f_name'] +page['f_endtype']

            with open(file_full_path, 'w') as target_file:
                target_file.write(template.render(content))

        logging.info('Page ' + index + ' created.')

if __name__ == "__main__":
    main()
