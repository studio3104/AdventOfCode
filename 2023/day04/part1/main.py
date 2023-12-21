import re


def parse_card(card: str) -> tuple[set[str], set[str]]:
    _, card_numbers = re.split(r':\s+', card)
    winning_numbers, owned_numbers = re.split(r'\s+\|\s+', card_numbers)
    return set(re.split(r'\s+', winning_numbers)), set(re.split(r'\s+', owned_numbers))


def calculate_point(cards: str) -> int:
    total = 0

    for card in cards.split('\n'):
        winning_numbers, owned_numbers = parse_card(card)
        if (won_count := len(winning_numbers & owned_numbers)) > 0:
            total += 1 << (won_count - 1)

    return total


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(calculate_point(f.read()))
