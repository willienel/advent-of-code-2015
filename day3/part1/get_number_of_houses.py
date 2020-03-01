import os


def get_number_of_houses(directions):

    visited_houses = dict()

    coordinate_x = 0
    coordinate_y = 0

    visited_houses[(coordinate_x, coordinate_y)] = 1

    for direction in directions:

        if direction == '<':
            coordinate_x -= 1
        elif direction == '>':
            coordinate_x += 1
        elif direction == '^':
            coordinate_y -= 1
        elif direction == 'v':
            coordinate_y += 1

        visited_houses[(coordinate_x, coordinate_y)] = 1

    return len(visited_houses.keys())


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = list(input_file.readline())

    print(get_number_of_houses(d))
