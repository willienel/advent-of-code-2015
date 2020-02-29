import os


def get_required_amount_of_ribbon(dimensions):

    required_amount_of_ribbon = 0

    for dimension in dimensions:

        length, width, height = dimension

        shortest_side, second_shortest_side = sorted([length, width, height])[:2]

        present_amount_required = shortest_side * 2 + second_shortest_side * 2
        bow_amount_required = length * width * height

        required_amount_of_ribbon += present_amount_required + bow_amount_required

    return required_amount_of_ribbon


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:

        d = list()

        for line in input_file.readlines():
            d.append(list(map(int, line.strip().split("x"))))

    print(get_required_amount_of_ribbon(d))
