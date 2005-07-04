# -*- coding: iso-8859-1 -*-
# Copyright (C) 2001-2005  Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
Handle for uncheckable application-specific links.
"""

import urlbase

class IgnoredUrl (urlbase.UrlBase):
    """
    Some schemes are defined in <http://www.w3.org/Addressing/schemes>.
    """

    def local_check (self):
        """
        Only logs that this URL is ignored.
        """
        self.set_extern(self.url)
        if self.extern[0] and self.extern[1]:
            self.add_info(_("Outside of domain filter, checked only syntax."))
        else:
            self.add_warning(_("%s URL ignored.") % self.scheme.capitalize())

    def can_get_content (self):
        """
        Ignored URLs have no content.

        @return: False
        @rtype: bool
        """
        return False
