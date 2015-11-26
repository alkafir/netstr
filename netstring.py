#!/usr/bin/env python3

"""
    Netstrings module for Python 3
    Copyright (C) 2015  Alfredo Mungo <alfredo.mungo@openmailbox.org>

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

    -----------------------------------------------------------------------------------------

    Netstrings specification: http://cr.yp.to/proto/netstrings.txt
"""

if __name__ == '__main__':
  import sys
  sys.exit('This is a Python module and not intended to be run as a standalone application')

_ASCII_COLON, _ASCII_COMMA = ':,'.encode('ascii')

def encode(s):
  """
    Encodes a string to a netstring, returning the corresponding bytes object.
  """
  return (str(len(s)) + ':' + s + ',').encode('ascii')

def decode(b):
  """
    Decodes the first netstring in the provided bytes object, returning the corresponding string object.
    
    THROWS:
      ValueError if the provided bytes object does not begin with a valid netstring
  """
    slen, s = b.split(_ASCII_COLON, 1)
    slen = int(slen)

    if slen < 0 or s[slen] != _ASCII_COMMA:
      raise ValueError

    return s[1:1+slen].decode('ascii')

def size(b):
  """
    Returns the size in bytes of the first netstring in the provided bytes object.
    WARNING: This function doesn't check for netstring validity.

    THROWS:
      ValueError if something goes wrong
  """
    try:
      slen = b[:b.find(_ASCII_COLON)].decode('ascii')

      return 2 + len(slen) + int(slen)
    except:
      raise ValueError
