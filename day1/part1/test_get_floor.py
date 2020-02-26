import unittest

from day1.part1.get_floor import get_floor


class TestGetFloor(unittest.TestCase):

    def test_get_floor_with_no_instructions_returns_zero(self):

        expected_value = 0
        instructions = []

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_opening_instruction_returns_one(self):

        expected_value = 1
        instructions = ['(']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_closing_instruction_returns_negative_one(self):

        expected_value = -1
        instructions = [')']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_two_open_instructions_returns_two(self):

        expected_value = 2
        instructions = ['(', '(']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_two_close_instructions_returns_negative_two(self):

        expected_value = -2
        instructions = [')', ')']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_opening_and_closing_instruction_returns_zero(self):

        expected_value = 0
        instructions = ['(', ')']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_two_opening_and_one_closing_instruction_returns_one(self):

        expected_value = 1
        instructions = ['(', '(', ')']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)

    def test_get_floor_with_one_opening_and_two_closing_instructions_returns_negative_one(self):

        expected_value = -1
        instructions = ['(', ')', ')']

        value = get_floor(instructions)

        self.assertEqual(expected_value, value)
