import os


def get_required_amount(dimensions):

    required_amount = 0

    for dimension in dimensions:

        length, width, height = dimension

        side_length_width = length * width
        side_width_height = width * height
        side_height_length = height * length

        side_smallest = min([side_length_width, side_width_height, side_height_length])

        area_length_width = 2 * side_length_width
        area_width_height = 2 * side_width_height
        area_height_length = 2 * side_height_length

        total_area = area_length_width + area_width_height + area_height_length

        required_amount += total_area + side_smallest

    return required_amount


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:

        d = list()

        for line in input_file.readlines():
            d.append(list(map(int, line.strip().split("x"))))

    print(get_required_amount(d))
