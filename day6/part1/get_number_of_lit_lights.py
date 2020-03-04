import os
import re


def get_number_of_lit_lights(instructions):

    lights_on = 0

    lights = [[False for i in range(1000)] for j in range(1000)]

    for instruction in instructions:

        action, start, end = instruction

        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):

                if action == "turn on":
                    lights[i][j] = True
                elif action == "turn off":
                    lights[i][j] = False
                elif action == "toggle":
                    lights[i][j] = not lights[i][j]

    for i in range(len(lights)):
        for j in range(len(lights[i])):
            if lights[i][j]:
                lights_on += 1

    return lights_on


if __name__ == '__main__':

    search_regex = r"(turn on|turn off|toggle)\s([0-9]{1,3},[0-9]{1,3})\sthrough\s([0-9]{1,3},[0-9]{1,3})"

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:

        d = []

        for line in input_file.readlines():

            result = re.search(search_regex, line)

            if result:
                action = result.group(1)
                start1, start2 = list(map(int, result.group(2).split(",")))
                end1, end2 = list(map(int, result.group(3).split(",")))

                d.append((action, (start1, start2), (end1, end2)))

    print(get_number_of_lit_lights(d))
