import os


def get_position(directions):

    direction_values = {'(': 1, ')': -1}

    floor = 0
    position = 0

    for direction in directions:
        position += 1
        floor += direction_values[direction]
        if floor < 0:
            return position

    return position


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = list(input_file.readline())

    print(get_position(d))
