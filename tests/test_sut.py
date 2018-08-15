import unittest
from source import sut


class TestSUT(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(True, True)

	def test_london(self):
		london = sut.London()
		self.assertEqual("Londres", london.say_spanish_name())
