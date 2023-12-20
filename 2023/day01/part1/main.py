def calibrate(values: str) -> int:
    value = 0

    for line in values.split('\n'):
        ones_digit = -1
        tens_digit = -1

        for c in line:
            if c.isdigit():
                n = int(c)
                ones_digit = n

                if tens_digit == -1:
                    tens_digit = n

        value += tens_digit * 10 + ones_digit

    return value


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(calibrate(f.read()))
