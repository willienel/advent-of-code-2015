import os


def get_number_of_houses(directions):

    visited_houses = set()

    coordinate_x_santa = 0
    coordinate_y_santa = 0
    coordinate_x_robot = 0
    coordinate_y_robot = 0

    visited_houses.add((coordinate_x_santa, coordinate_y_santa))
    visited_houses.add((coordinate_x_robot, coordinate_y_robot))

    for index, direction in enumerate(directions):

        if index % 2 == 0:
            is_santa = True
        else:
            is_santa = False

        if direction == '<':
            if is_santa:
                coordinate_x_santa += -1
            else:
                coordinate_x_robot += -1
        elif direction == '>':
            if is_santa:
                coordinate_x_santa += 1
            else:
                coordinate_x_robot += 1
        elif direction == '^':
            if is_santa:
                coordinate_y_santa += -1
            else:
                coordinate_y_robot += -1
        elif direction == 'v':
            if is_santa:
                coordinate_y_santa += 1
            else:
                coordinate_y_robot += 1

        visited_houses.add((coordinate_x_santa, coordinate_y_santa))
        visited_houses.add((coordinate_x_robot, coordinate_y_robot))

    return len(visited_houses)


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = list(input_file.readline())

    print(get_number_of_houses(d))
