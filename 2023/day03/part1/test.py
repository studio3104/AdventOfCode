import pytest
import textwrap

from .main import find_parts_and_sum_ids


@pytest.mark.parametrize(('schematic', 'expected'), (
        (
                textwrap.dedent('''
                467..114..
                ...*......
                ..35..633.
                ......#...
                617*......
                .....+.58.
                ..592.....
                ......755.
                ...$.*....
                .664.598..
                ''').strip(),
                4361,
        ),
))
def test_find_parts_and_sum_ids(schematic: str, expected: int):
    assert find_parts_and_sum_ids(schematic) == expected
