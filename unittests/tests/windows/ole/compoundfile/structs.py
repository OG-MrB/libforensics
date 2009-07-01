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
Unit tests for the lf.os.windows.ole.structs module

.. moduleauthor:: Michael Murr (mmurr@codeforensics.net)
"""

__docformat__ = "restructuredtext en"

from unittest import TestCase, main
from lf.struct.extract import extractor_factory as factory
from lf.windows.ole.compoundfile.structs import Header, DirEntry

header_str = \
    b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1\x00\x00\x00\x00\x00\x00\x00\x00"\
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x00\x03\x00\xFE\xFF\x09\x00"\
    b"\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00"\
    b"\x7A\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x7C\x00\x00\x00"\
    b"\x01\x00\x00\x00\xFE\xFF\xFF\xFF\x00\x00\x00\x00\x79\x00\x00\x00"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"\
    b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"


dir_entry_str = \
    b"\x52\x00\x6F\x00\x6F\x00\x74\x00\x20\x00\x45\x00\x6E\x00\x74\x00"\
    b"\x72\x00\x79\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\
    b"\x16\x00\x05\x01\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x03\x00\x00\x00"\
    b"\x06\x09\x02\x00\x00\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x46"\
    b"\x00\x00\x00\x00\xEE\xC6\x64\x87\x74\xCB\xC2\x01\x10\x0D\x9B\xFB"\
    b"\x75\xCB\xC2\x01\x7D\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00"

class HeaderTestCase():
    def setUp(self):
        self.extractor = factory.make(Header())
    # end def setUp

    def test_values(self):
        ae = self.assertEqual

        header = self.extractor.extract(header_str)

        ae(header.sig, b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1")
        ae(header.clsid.data1, 0)
        ae(header.clsid.data2, 0)
        ae(header.clsid.data3, 0)
        ae(header.clsid.data4, (0, 0, 0, 0, 0, 0, 0, 0))
        ae(header.ver_minor, 0x3E)
        ae(header.ver_major, 3)
        ae(header.byte_order, 0xFFFE)
        ae(header.sect_shift, 9)
        ae(header.mini_sect_shift, 6)
        ae(header.rsvd, b"\x00\x00\x00\x00\x00\x00")
        ae(header.dir_count, 0)
        ae(header.fat_count, 1)
        ae(header.dir_sect, 1)
        ae(header.trans_num, 0)
        ae(header.mini_stream_cutoff, 0x1000)
        ae(header.mini_fat_sect, 2)
        ae(header.mini_fat_count, 1)
        ae(header.di_fat_sect, 0xFFFFFFFE)
        ae(header.di_fat_count, 0)
        ae(len(header.di_fat), 109)
        ae(header.di_fat[0], 0)

        for index in range(1, 109):
            ae(header.di_fat[index], 0xFFFFFFFF)
        # end for
    # end def test_values
# end class HeaderTestCase

class DirEntryTestCase(TestCase):
    def setUp(self):
        self.extractor = factory.make(DirEntry())
    # end def setUp

    def test_values(self):
        ae = self.assertEqual

        dir_entry = self.extractor.extract(dir_entry_str)
        ae(dir_entry.name, dir_entry_str[:64])
        ae(dir_entry.name_size, 22)
        ae(dir_entry.type, 5)
        ae(dir_entry.color, 1)
        ae(dir_entry.left_sid, 0xFFFFFFFF)
        ae(dir_entry.right_sid, 0xFFFFFFFF)
        ae(dir_entry.child_sid, 3)
        ae(dir_entry.clsid.data1, 0x20906)
        ae(dir_entry.clsid.data2, 0)
        ae(dir_entry.clsid.data3, 0)
        ae(dir_entry.clsid.data4, (192, 0, 0, 0, 0, 0, 0, 70))
        ae(dir_entry.state, 0)
        ae(dir_entry.btime.lo, 0x8764C6EE)
        ae(dir_entry.btime.hi, 0x1C2CB74)
        ae(dir_entry.mtime.lo, 0xFB9B0D10)
        ae(dir_entry.mtime.hi, 0x01C2CB75)
        ae(dir_entry.first_sect, 125)
        ae(dir_entry.size, 128)
    # end def test_values
# end class DirEntryTestCase

if __name__ == "__main__":
    main()
# end if
