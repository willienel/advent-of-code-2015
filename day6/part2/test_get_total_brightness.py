import unittest

from day6.part2.get_total_brightness import get_total_brightness


class TestGetTotalBrightness(unittest.TestCase):

    def test_get_total_brightness_example_1(self):

        expected_value = 1
        instructions = [("turn on", (0, 0), (0, 0))]

        value = get_total_brightness(instructions)

        self.assertEqual(expected_value, value)

    def test_get_total_brightness_example_2(self):

        expected_value = 2000000
        instructions = [("toggle", (0, 0), (999, 999))]

        value = get_total_brightness(instructions)

        self.assertEqual(expected_value, value)
