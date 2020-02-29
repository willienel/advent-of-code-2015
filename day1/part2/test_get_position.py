import unittest

from day1.part2.get_position import get_position


class TestPositionFloor(unittest.TestCase):

    def test_get_position_example_1(self):

        expected_value = 1
        directions = list(")")

        value = get_position(directions)

        self.assertEqual(expected_value, value)

    def test_get_position_example_2(self):

        expected_value = 5
        directions = list('()())')

        value = get_position(directions)

        self.assertEqual(expected_value, value)
