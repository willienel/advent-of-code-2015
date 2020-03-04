import os


def get_nice_string_count(strings):

    nice_strings = set()

    for string in strings:

        pairs = dict()
        repeats = set()

        string = string.strip()
        string_length = len(string)

        for i in range(string_length):

            overlap = False

            first_character = string[i]
            second_character = string[i + 1] if i < string_length - 1 else ""
            third_character = string[i + 2] if i < string_length - 2 else ""

            if first_character == second_character == third_character:
                overlap = True

            pair = f"{first_character}{second_character}"
            combined_characters = f"{first_character}{second_character}{third_character}"

            if not overlap and len(pair) == 2:

                if pair not in pairs:
                    pairs[pair] = 0

                pairs[pair] += 1

            if not overlap and first_character == third_character:
                repeats.add(combined_characters)

        has_pair = False
        has_repeat = False

        for key in pairs.keys():
            if pairs[key] >= 2:
                has_pair = True
                break

        if len(repeats) >= 1:
            has_repeat = True

        if has_pair and has_repeat:
            nice_strings.add(string)

    return len(nice_strings)


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = input_file.readlines()

    print(get_nice_string_count(d))
