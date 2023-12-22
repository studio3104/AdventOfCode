from day04.part1.main import parse_card


def count_cards(cards: str) -> int:
    card_list = cards.split('\n')
    num_cards = [1 for _ in card_list]

    for i, card in enumerate(card_list):
        winning_numbers, owned_numbers = parse_card(card)
        if (won_count := len(winning_numbers & owned_numbers)) == 0:
            continue

        for j in range(i + 1, min(i + won_count + 1, len(num_cards))):
            num_cards[j] += num_cards[i]

    return sum(num_cards)


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(count_cards(f.read()))
