from unittest import TestCase

from day7.part1.get_signal_for_wire import get_signal_for_wire


class TestGetSignalForWire(TestCase):

    def test_get_signal_for_wire_1(self):

        expected_value = 72
        instructions = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d"
        ]

        value = get_signal_for_wire(instructions, "d")

        self.assertEqual(expected_value, value)

    def test_get_signal_for_wire_2(self):

        expected_value = 507
        instructions = [
            "123 -> x",
            "456 -> y",
            "x OR y -> e"
        ]

        value = get_signal_for_wire(instructions, "e")

        self.assertEqual(expected_value, value)

    def test_get_signal_for_wire_3(self):

        expected_value = 492
        instructions = [
            "123 -> x",
            "456 -> y",
            "x LSHIFT 2 -> f"
        ]

        value = get_signal_for_wire(instructions, "f")

        self.assertEqual(expected_value, value)

    def test_get_signal_for_wire_4(self):

        expected_value = 114
        instructions = [
            "123 -> x",
            "456 -> y",
            "y RSHIFT 2 -> g"
        ]

        value = get_signal_for_wire(instructions, "g")

        self.assertEqual(expected_value, value)

    def test_get_signal_for_wire_5(self):

        expected_value = -124
        instructions = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h"
        ]

        value = get_signal_for_wire(instructions, "h")

        self.assertEqual(expected_value, value)

    def test_get_signal_for_wire_6(self):

        expected_value = -457
        instructions = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT y -> i"
        ]

        value = get_signal_for_wire(instructions, "i")

        self.assertEqual(expected_value, value)
