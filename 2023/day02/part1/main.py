def sum_possible_game_id_nums(results: str) -> int:
    total_count = 0
    resources = {'red': 12, 'green': 13, 'blue': 14}

    for line in results.split('\n'):
        game, result = line.split(': ')
        _, game_id = game.split(' ')
        game_id = int(game_id)

        if all(
                int(num) <= resources[color]
                for turns in result.split('; ')
                for act in turns.split(', ')
                for num, color in [act.split(' ')]
        ):
            total_count += game_id

    return total_count


if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../input.txt')) as f:
        print(sum_possible_game_id_nums(f.read()))
