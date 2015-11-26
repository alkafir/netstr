#!/usr/bin/env python3

import unittest
import netstring

class TestCase(unittest.TestCase):
  def setUp(self):
    self.junk = b'junkdata' * 10
    self.binary_data = b'12:\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64\x21,' + self.junk
    self.ascii_data = 'hello world!'

  def test_length(self):
    self.assertEqual(netstring.length(self.binary_data), len(self.ascii_data))

  def test_size(self):
    self.assertEqual(netstring.size(self.binary_data), len(self.binary_data) - len(self.junk))

  def test_encode(self):
    self.assertEqual(netstring.encode(self.ascii_data), self.binary_data[:-len(self.junk)])

  def test_decode(self):
    self.assertEqual(netstring.decode(self.binary_data), self.ascii_data)

if __name__ == '__main__':
  unittest.main()
