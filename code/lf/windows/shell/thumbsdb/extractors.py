# Copyright 2009 Michael Murr
#
# This file is part of LibForensics.
#
# LibForensics is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LibForensics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with LibForensics.  If not, see <http://www.gnu.org/licenses/>.

"""
Extractors for Thumbs.db data structures.

.. moduleauthor:: Michael Murr (mmurr@codeforensics.net)
"""

__docformat__ = "restructuredtext en"
__all__ = [
    "catalog_header", "catalog_entry_header", "entry_header",
    "entry_header_old"
]

from lf.struct.extract import extractor_factory as factory
from lf.windows.shell.thumbsdb.structs import (
    CatalogHeader, CatalogEntryHeader, EntryHeader, EntryHeaderOld
)

catalog_header = factory.make(CatalogHeader())
catalog_entry_header = factory.make(CatalogEntryHeader())
entry_header = factory.make(EntryHeader())
entry_header_old = factory.make(EntryHeaderOld())
