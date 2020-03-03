import os


def get_nice_string_count(strings):

    nice_strings = set()

    vowels = ["a", "e", "i", "o", "u"]
    naughty_strings = ["ab", "cd", "pq", "xy"]

    for string in strings:

        string_vowels = []
        string_consecutive_letters = []
        string_naughty_words = []

        string = string.strip()
        string_length = len(string)

        for i in range(string_length):

            first_character = string[i]
            second_character = string[i + 1] if i < string_length - 1 else ""

            combined_characters = f"{first_character}{second_character}"

            if combined_characters in naughty_strings:
                string_naughty_words.append(combined_characters)

            if first_character in vowels:
                string_vowels.append(first_character)

            if first_character == second_character:
                string_consecutive_letters.append(combined_characters)

        if len(string_naughty_words) == 0:
            if len(string_vowels) >= 3 and len(string_consecutive_letters) >= 1:
                nice_strings.add(string)

    return len(nice_strings)


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = input_file.readlines()

    print(get_nice_string_count(d))
