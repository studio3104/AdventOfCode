from functools import reduce
from operator import mul

from day03.part1.main import fetch_part_id, get_adjacent_positions


def _calculate_gear_ratio(schematic: list[list[str]]) -> int:
    total = 0

    for i, row in enumerate(schematic):
        for j, segment in enumerate(row):
            if segment != '*':
                continue

            checked = set()
            part_ids = []

            for pos in get_adjacent_positions(i, j):
                if (part_id := fetch_part_id(pos, schematic, checked)) == 0:
                    continue
                part_ids.append(part_id)

            if len(part_ids) != 2:
                continue

            total += reduce(mul, part_ids)

    return total


def calculate_gear_ratio(schematic: str) -> int:
    return _calculate_gear_ratio([list(row) for row in schematic.split('\n')])


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(calculate_gear_ratio(f.read()))
