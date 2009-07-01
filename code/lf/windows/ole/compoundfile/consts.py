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
Constants for Microsoft's OLE structured storage files.

.. moduleauthor:: Michael Murr (mmurr@codeforensics.net)
"""

__docformat__ = "restructuredtext en"
__all__ = [
    "HEADER_SIG", "BYTE_ORDER_LITTLE_ENDIAN", "FAT_EOC", "FAT_UNALLOC",
    "FAT_FAT_SECT", "FAT_DIF_SECT", "STGTY_INVALID", "STGTY_STORAGE",
    "STGTY_STREAM", "STGTY_LOCKBYTES", "STGTY_PROPERTY", "STGTY_ROOT",
    "DE_RED", "DE_BLACK", "STREAM_ID_MIN", "STREAM_ID_MAX", "STREAM_ID_NONE"
]

HEADER_SIG = "\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1"
BYTE_ORDER_LITTLE_ENDIAN = 0xFFFE

FAT_EOC = 0xFFFFFFFE
FAT_UNALLOC = 0xFFFFFFFF
FAT_FAT_SECT = 0xFFFFFFFD
FAT_DIF_SECT = 0xFFFFFFC

TYPE_INVALID = 0
TYPE_STORAGE = 1
TYPE_STREAM = 2
TYPE_LOCKBYTES = 3
TYPE_PROPERTY = 4
TYPE_ROOT = 5

DE_RED = 0
DE_BLACK = 1

STREAM_ID_MIN = 0
STREAM_ID_MAX = 0xFFFFFFFA
STREAM_ID_NONE = 0xFFFFFFFF
