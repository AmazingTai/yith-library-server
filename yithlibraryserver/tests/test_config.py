# Yith Library Server is a password storage server.
# Copyright (C) 2012 Yaco Sistemas
# Copyright (C) 2012 Alejandro Blanco Escudero <alejandro.b.e@gmail.com>
# Copyright (C) 2012 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# This file is part of Yith Library Server.
#
# Yith Library Server is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Yith Library Server is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Yith Library Server.  If not, see <http://www.gnu.org/licenses/>.

import os
import unittest

from yithlibraryserver.config import read_setting_from_env


class ConfigTests(unittest.TestCase):

    def test_read_setting_from_env(self):
        settings = {
            'foo_bar': '1',
            }

        self.assertEqual('1', read_setting_from_env(settings, 'foo_bar'))

        self.assertEqual('default',
                         read_setting_from_env(settings, 'new_option', 'default'))
        self.assertEqual(None,
                         read_setting_from_env(settings, 'new_option'))

        os.environ['FOO_BAR'] = '2'
        self.assertEqual('2', read_setting_from_env(settings, 'foo_bar'))
