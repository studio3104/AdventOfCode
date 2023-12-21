def find_leftmost_digit_position(position: tuple[int, int], schematic: list[list[str]]) -> tuple[int, int]:
    _next = (position[0], position[1] - 1)
    if _next[1] < 0 or not schematic[_next[0]][_next[1]].isdigit():
        return position
    return find_leftmost_digit_position(_next, schematic)


def _fetch_part_id(position: tuple[int, int], schematic: list[list[str]], checked: set[tuple[int, int]], _id: int = 0) -> int:
    if position[1] >= len(schematic[0]) or not schematic[position[0]][position[1]].isdigit():
        return _id
    checked.add(position)
    current = _id * 10 + int(schematic[position[0]][position[1]])
    return _fetch_part_id((position[0], position[1] + 1), schematic, checked, current)


def fetch_part_id(position: tuple[int, int], schematic: list[list[str]], checked: set[tuple[int, int]]) -> int:
    if (
            position in checked or
            position[0] < 0 or
            position[1] < 0 or
            position[0] >= len(schematic) or
            position[1] >= len(schematic[0]) or
            not schematic[position[0]][position[1]].isdigit()
    ):
        return 0

    p = find_leftmost_digit_position(position, schematic)
    return _fetch_part_id(p, schematic, checked)


def _find_parts_and_sum_ids(schematic: list[list[str]]) -> int:
    total = 0
    checked = set()

    for i, row in enumerate(schematic):
        for j, segment in enumerate(row):
            if segment.isdigit() or segment == '.':
                continue

            total += fetch_part_id((i - 1, j - 1), schematic, checked)
            total += fetch_part_id((i - 1, j), schematic, checked)
            total += fetch_part_id((i - 1, j + 1), schematic, checked)
            total += fetch_part_id((i, j - 1), schematic, checked)
            total += fetch_part_id((i, j + 1), schematic, checked)
            total += fetch_part_id((i + 1, j - 1), schematic, checked)
            total += fetch_part_id((i + 1, j), schematic, checked)
            total += fetch_part_id((i + 1, j + 1), schematic, checked)

    return total


def find_parts_and_sum_ids(schematic: str) -> int:
    return _find_parts_and_sum_ids([list(row) for row in schematic.split('\n')])


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(find_parts_and_sum_ids(f.read()))
