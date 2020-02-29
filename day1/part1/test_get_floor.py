import unittest

from day1.part1.get_floor import get_floor


class TestGetFloor(unittest.TestCase):

    def test_get_floor_example_1(self):

        expected_value = 0
        directions = list("(())")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_2(self):

        expected_value = 0
        directions = list("()()")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_3(self):

        expected_value = 3
        directions = list("(((")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_4(self):

        expected_value = 3
        directions = list("(()(()(")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_5(self):

        expected_value = 3
        directions = list("))(((((")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_6(self):

        expected_value = -1
        directions = list("())")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_7(self):

        expected_value = -1
        directions = list("))(")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_8(self):

        expected_value = -3
        directions = list(")))")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)

    def test_get_floor_example_9(self):

        expected_value = -3
        directions = list(")())())")

        value = get_floor(directions)

        self.assertEqual(expected_value, value)
