import unittest

from day2.part1.get_required_amount import get_required_amount


class TestGetRequiredAmount(unittest.TestCase):

    def test_get_required_amount_example_1(self):

        expected_value = 58
        sizes = [list(map(int, "2x3x4".split("x")))]

        value = get_required_amount(sizes)

        self.assertEqual(expected_value, value)

    def test_get_required_amount_example_2(self):

        expected_value = 43
        sizes = [list(map(int, "1x1x10".split("x")))]

        value = get_required_amount(sizes)

        self.assertEqual(expected_value, value)
