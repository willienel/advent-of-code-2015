import unittest

from day3.part2.get_number_of_houses import get_number_of_houses


class TestGetNumberOfHouses(unittest.TestCase):

    def test_get_number_of_houses_example_1(self):

        expected_value = 3
        directions = list("^v")

        value = get_number_of_houses(directions)

        self.assertEqual(expected_value, value)

    def test_get_number_of_houses_example_2(self):

        expected_value = 3
        directions = list("^>v<")

        value = get_number_of_houses(directions)

        self.assertEqual(expected_value, value)

    def test_get_number_of_houses_example_3(self):

        expected_value = 11
        directions = list("^v^v^v^v^v")

        value = get_number_of_houses(directions)

        self.assertEqual(expected_value, value)
