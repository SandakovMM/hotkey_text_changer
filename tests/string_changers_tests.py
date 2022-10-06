#!/usr/bin/python3

import sys

print(sys.path)

import unittest

from changers.string_changers import *

class TestDotAdder(unittest.TestCase):
	def test_simple(self):
		self.assertEqual(string_add_dots('test'), 't.e.s.t.')

	def test_empty(self):
		self.assertEqual(string_add_dots(''), '')

	def test_none(self):
		self.assertEqual(string_add_dots(None), None)

	def test_one_symbol(self):
		self.assertEqual(string_add_dots('t'), 't.')

class TestCalculateLength(unittest.TestCase):
	def test_simple(self):
		self.assertEqual(string_calculate_length('test'), '4')

	def test_empty(self):
		self.assertEqual(string_calculate_length(''), '0')

	def test_none(self):
		self.assertEqual(string_calculate_length(None), None)

if __name__ == '__main__':
	unittest.main()