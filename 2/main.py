ALLOWED_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main():
    total1 = 0
    total2 = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            game = parse_line(line)
            total1 = total1 + is_game_possible(game)
            total2 = total2 + get_pwr_of_min_set(game)

    print(total1)
    print(total2)


def parse_line(line: str) -> tuple:
    """
    game_num : {
        [ [(num, color)... ]... ] # rounds
    }
    """
    game, rounds = line.strip().split(":")
    junk, game_num = game.split(" ")
    rounds = [[tuple(dice.strip().split(" ")) for dice in round_.split(",")] for round_ in rounds.split(";")]

    return game_num, rounds


def is_game_possible(game: tuple) -> int:
    # print(game)
    game_num, rounds = game
    for round_ in rounds:
        for num, color in round_:
            if int(num) > ALLOWED_CUBES[color]:
                return 0

    return int(game_num)


def get_pwr_of_min_set(game: tuple) -> int:
    color_counts = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    game_num, rounds = game
    for round_ in rounds:
        for num, color in round_:
            if color_counts[color] < int(num):
                color_counts[color] = int(num)

    return color_counts["red"] * color_counts["green"] * color_counts["blue"]


if __name__ == "__main__":
    # print(timeit(main, number=1))
    main()
