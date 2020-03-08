import os


def get_signal_for_wire(instructions, signal_value_to_fetch):

    signal_values = dict()

    while signal_value_to_fetch not in signal_values:

        for instruction in instructions:

            input_instruction, output_instruction = instruction.split("->")

            input_instruction = input_instruction.strip()
            output_instruction = output_instruction.strip()

            input_instruction_length = 1 if input_instruction.isdigit() else len(input_instruction.split(" "))

            if input_instruction_length == 1:
                if input_instruction.isdigit():
                    signal_values[output_instruction] = int(input_instruction)
                elif input_instruction in signal_values:
                    signal_values[output_instruction] = int(signal_values[input_instruction])
            elif input_instruction_length == 2:

                operation, key = input_instruction.split(" ")

                if key not in signal_values:
                    continue

                signal_value = int(signal_values.get(key, 0))

                if operation == "NOT":
                    signal_values[output_instruction] = ~signal_value
            else:

                key1, operation, key2 = input_instruction.split(" ")

                if not key1.isdigit() and key1 not in signal_values:
                    continue

                if not key2.isdigit() and key2 not in signal_values:
                    continue

                signal_value1 = int(signal_values.get(key1, key1))
                signal_value2 = int(signal_values.get(key2, key2))

                if operation == "AND":
                    signal_values[output_instruction] = signal_value1 & signal_value2
                elif operation == "OR":
                    signal_values[output_instruction] = signal_value1 | signal_value2
                elif operation == "LSHIFT":
                    signal_values[output_instruction] = signal_value1 << signal_value2
                elif operation == "RSHIFT":
                    signal_values[output_instruction] = signal_value1 >> signal_value2

    return signal_values[signal_value_to_fetch]


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = input_file.readlines()

    print(get_signal_for_wire(d, "a"))
