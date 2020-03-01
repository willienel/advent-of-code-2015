import unittest

from day3.part1.get_number_of_houses import get_number_of_houses


class TestGetNumberOfHouses(unittest.TestCase):

    def test_get_number_of_houses_example_1(self):

        expected_value = 2
        directions = list(">")

        value = get_number_of_houses(directions)

        self.assertEqual(expected_value, value)

    def test_get_number_of_houses_example_2(self):

        expected_value = 4
        directions = list("^>v<")

        value = get_number_of_houses(directions)

        self.assertEqual(expected_value, value)
