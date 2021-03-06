import os


def get_floor(directions):

    direction_values = {'(': 1, ')': -1}

    floor = 0

    for direction in directions:
        floor += direction_values[direction]

    return floor


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = list(input_file.readline())

    print(get_floor(d))
