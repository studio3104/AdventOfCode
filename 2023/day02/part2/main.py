import math


def calc_power_of_set(results: str) -> int:
    total_power = 0

    for line in results.split('\n'):
        _, result = line.split(': ')
        color_requirements = {'red': 0, 'green': 0, 'blue': 0}

        for act in result.replace('; ', ', ').split(', '):
            num, color = act.split(' ')
            color_requirements[color] = max(color_requirements[color], int(num))

        total_power += math.prod(color_requirements.values())

    return total_power


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(calc_power_of_set(f.read()))
