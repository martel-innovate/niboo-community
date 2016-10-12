# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Gael Rabier
#    Copyright 2016 Niboo SPRL
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Project - Task Identifier',
    'category': "Generic Modules/Others",
    'summary': 'Add an identifier on tasks (project-sequence number)',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        Project Task Identifier allows you to select an identifier for customers.
        This identifier will be used to generate a unique key for all project tasks related to the customer, making it easier to identify tasks.
        """,
    'author': 'Niboo',
    'depends': ['project'],
    'data': [
        'views/project_task_view.xml',
        'views/res_partner_view.xml',
    ],
    'qweb': [],
    'images': [
        'static/description/project_task_identifier_cover.png',
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
