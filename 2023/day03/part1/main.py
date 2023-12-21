def find_leftmost_digit_position(position: tuple[int, int], schematic: list[list[str]]) -> tuple[int, int]:
    x, y = position
    while y > 0 and schematic[x][y - 1].isdigit():
        y -= 1
    return x, y


def fetch_part_id(position: tuple[int, int], schematic: list[list[str]], checked: set[tuple[int, int]]) -> int:
    if (
            position in checked or
            not (0 <= position[0] < len(schematic)) or
            not (0 <= position[1] < len(schematic[0])) or
            not schematic[position[0]][position[1]].isdigit()
    ):
        return 0

    leftmost_position = find_leftmost_digit_position(position, schematic)
    x, y = leftmost_position
    part_id = 0

    while y < len(schematic[0]) and schematic[x][y].isdigit():
        part_id = part_id * 10 + int(schematic[x][y])
        checked.add((x, y))
        y += 1

    return part_id


def get_adjacent_positions(i: int, j: int) -> list[tuple[int, int]]:
    return [(i + dx, j + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]


def _find_parts_and_sum_ids(schematic: list[list[str]]) -> int:
    total = 0
    checked = set()

    for i, row in enumerate(schematic):
        for j, segment in enumerate(row):
            if segment.isdigit() or segment == '.':
                continue

            for pos in get_adjacent_positions(i, j):
                total += fetch_part_id(pos, schematic, checked)

    return total


def find_parts_and_sum_ids(schematic: str) -> int:
    return _find_parts_and_sum_ids([list(row) for row in schematic.split('\n')])


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(find_parts_and_sum_ids(f.read()))
