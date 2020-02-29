import unittest

from day2.part2.get_required_amount_of_ribbon import get_required_amount_of_ribbon


class TestGetRequiredAmountOfRibbon(unittest.TestCase):

    def test_get_required_amount_of_ribbon_example_1(self):

        expected_value = 34
        dimensions = [list(map(int, "2x3x4".split("x")))]

        value = get_required_amount_of_ribbon(dimensions)

        self.assertEqual(expected_value, value)

    def test_get_required_amount_of_ribbon_example_2(self):

        expected_value = 14
        dimensions = [list(map(int, "1x1x10".split("x")))]

        value = get_required_amount_of_ribbon(dimensions)

        self.assertEqual(expected_value, value)
