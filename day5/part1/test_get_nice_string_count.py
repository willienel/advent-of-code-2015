import unittest

from day5.part1.get_nice_string_count import get_nice_string_count


class TestGetNiceStringCount(unittest.TestCase):

    def test_get_nice_string_count_example_1(self):

        expected_value = 1
        strings = ["ugknbfddgicrmopn"]

        value = get_nice_string_count(strings)

        self.assertEqual(expected_value, value)

    def test_get_nice_string_count_example_2(self):

        expected_value = 1
        strings = ["aaa"]

        value = get_nice_string_count(strings)

        self.assertEqual(expected_value, value)

    def test_get_nice_string_count_example_3(self):

        expected_value = 0
        strings = ["jchzalrnumimnmhp"]

        value = get_nice_string_count(strings)

        self.assertEqual(expected_value, value)

    def test_get_nice_string_count_example_4(self):

        expected_value = 0
        strings = ["haegwjzuvuyypxyu"]

        value = get_nice_string_count(strings)

        self.assertEqual(expected_value, value)

    def test_get_nice_string_count_example_5(self):

        expected_value = 0
        strings = ["dvszwmarrgswjxmb"]

        value = get_nice_string_count(strings)

        self.assertEqual(expected_value, value)
