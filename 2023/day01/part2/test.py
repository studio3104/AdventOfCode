import pytest

from .main import calibrate


@pytest.mark.parametrize(('values', 'expected'), (
        (
                '''
                two1nine
                eightwothree
                abcone2threexyz
                xtwone3four
                4nineeightseven2
                zoneight234
                7pqrstsixteen
                '''.replace(' ', '').strip(),
                281,
        ),
        (
                '''
                vfzmncfonexxkzlcstqhxvtwoplsglsix1kpkssfz
                '''.replace(' ', '').strip(),
                11,
        ),
))
def test_calibrate(values: str, expected: int) -> None:
    assert calibrate(values) == expected
