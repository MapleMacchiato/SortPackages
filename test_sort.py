import unittest
from package_sort import sort


class TestPackageSort(unittest.TestCase):

    def test_zero_width(self):
        with self.assertRaises(Exception):
            sort(0, 1, 1, 1)

    def test_zero_height(self):
        with self.assertRaises(Exception):
            sort(1, 0, 1, 1)

    def test_zero_length(self):
        with self.assertRaises(Exception):
            sort(1, 1, 0, 1)

    def test_zero_mass(self):
        with self.assertRaises(Exception):
            sort(1, 1, 1, 0)

    def test_bulky_width(self):
        self.assertEqual(sort(151, 1, 1, 1), "SPECIAL")

    def test_bulky_height(self):
        self.assertEqual(sort(1, 151, 1, 1), "SPECIAL")

    def test_bulky_volume(self):
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_bulky_length(self):
        self.assertEqual(sort(1, 1, 151, 1), "SPECIAL")

    def test_heavy_mass(self):
        self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")

    def test_special_bulky(self):
        self.assertEqual(sort(11, 10, 151, 15), "SPECIAL")

    def test_special_heavy(self):
        self.assertEqual(sort(1, 1, 1, 21), "SPECIAL")

    def test_normal(self):
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")
