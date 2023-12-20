def calibrate(values: str) -> int:
    total_value = 0

    for line in values.split('\n'):
        ones_digit, tens_digit = -1, -1
        last_matched_number = None

        for i, char in enumerate(line):
            if char.isdigit():
                last_matched_number = int(char)
            else:
                if i + 2 >= len(line) or char not in ('e', 'f', 'n', 'o', 's', 't'):
                    continue
                word = f'{char}{line[i + 1]}{line[i + 2]}'

                if word == 'one':
                    last_matched_number = 1
                elif word == 'two':
                    last_matched_number = 2
                elif word == 'six':
                    last_matched_number = 6

                if i + 3 < len(line):
                    word = f'{word}{line[i + 3]}'

                    if word == 'four':
                        last_matched_number = 4
                    elif word == 'five':
                        last_matched_number = 5
                    elif word == 'nine':
                        last_matched_number = 9

                if i + 4 < len(line):
                    word = f'{word}{line[i + 4]}'

                    if word == 'three':
                        last_matched_number = 3
                    elif word == 'seven':
                        last_matched_number = 7
                    elif word == 'eight':
                        last_matched_number = 8

            if last_matched_number is not None:
                ones_digit = last_matched_number
                if tens_digit == -1:
                    tens_digit = last_matched_number

        total_value += tens_digit * 10 + ones_digit

    return total_value


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(calibrate(f.read()))
