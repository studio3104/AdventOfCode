import pytest
import textwrap

from .main import calculate_gear_ratio


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
                467835,
        ),
))
def test_calculate_gear_ratio(schematic: str, expected: int):
    assert calculate_gear_ratio(schematic) == expected
