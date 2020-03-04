import os
import re


def get_total_brightness(instructions):

    total_brightness = 0

    lights = [[0 for i in range(1000)] for j in range(1000)]

    for instruction in instructions:

        action, start, end = instruction

        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):

                if action == "turn on":
                    lights[i][j] += 1
                elif action == "turn off":
                    if lights[i][j] > 0:
                        lights[i][j] -= 1
                elif action == "toggle":
                    lights[i][j] += 2

    for i in range(len(lights)):
        for j in range(len(lights[i])):
            total_brightness += lights[i][j]

    return total_brightness


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

    print(get_total_brightness(d))
