def calibrate(values: str) -> int:
    total_value = 0

    for line in values.split('\n'):
        digits = [int(c) for c in line if c.isdigit()]
        total_value += digits[0] * 10 + digits[-1]

    return total_value


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(calibrate(f.read()))
