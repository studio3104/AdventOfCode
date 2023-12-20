import pytest

from .main import calibrate


@pytest.mark.parametrize(('values', 'expected'), (
        (
                '''
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
                '''.replace(' ', '').strip(),
                142,
        ),
))
def test_calibrate(values: str, expected: int) -> None:
    assert calibrate(values) == expected
