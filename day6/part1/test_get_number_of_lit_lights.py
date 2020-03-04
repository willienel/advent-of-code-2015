import unittest

from day6.part1.get_number_of_lit_lights import get_number_of_lit_lights


class TestGetNumberOfLitLights(unittest.TestCase):

    def test_get_number_of_lit_lights_example_1(self):

        expected_value = 1000000
        instructions = [("turn on", (0, 0), (999, 999))]

        value = get_number_of_lit_lights(instructions)

        self.assertEqual(expected_value, value)

    def test_get_number_of_lit_lights_example_2(self):

        expected_value = 1000
        instructions = [("toggle", (0, 0), (999, 0))]

        value = get_number_of_lit_lights(instructions)

        self.assertEqual(expected_value, value)

    def test_get_number_of_lit_lights_example_3(self):

        expected_value = 0
        instructions = [("turn off", (499, 499), (500, 500))]

        value = get_number_of_lit_lights(instructions)

        self.assertEqual(expected_value, value)
