import unittest

from day4.part1and2.get_lowest_number import get_lowest_number


class TestGetLowestNumber(unittest.TestCase):

    def test_get_lowest_number_example_1(self):

        expected_value = 609043
        secret_key = "abcdef"

        value = get_lowest_number(secret_key)

        self.assertEqual(expected_value, value)

    def test_get_lowest_number_example_2(self):

        expected_value = 1048970
        secret_key = "pqrstuv"

        value = get_lowest_number(secret_key)

        self.assertEqual(expected_value, value)
