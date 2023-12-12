def main():
    with open("input.txt", "r") as f:
        lines = [ln.strip() for ln in f]

    print(solve_1(lines))
    print(solve_2(lines))


def solve_1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        card, win, mine = parse_line(line)
        intersection = list(set(win) & set(mine))
        points = 0
        for _ in intersection:
            points = points * 2 if points > 0 else 1
        total += points
    return total


def solve_2(lines: list[str]) -> int:
    cards = {}
    multipliers = {}
    # load into dict
    for line in lines:
        card, win, mine = parse_line(line)
        cards[card] = win, mine

    # this could probably be done with smarter math 🤷
    for card, (win, mine) in cards.items():
        multiplier = multipliers.setdefault(card, 1)
        intersection = list(set(win) & set(mine))
        # set multipliers on next cards
        for i in range(1, len(intersection) + 1):
            multipliers[card + i] = multipliers.setdefault(card + i, 1) + multiplier
        # print(f"{card} x{multiplier} {intersection}")
        # print(f"{card} x{multiplier} {intersection} {multipliers}")

    return sum([n for n in multipliers.values()])


def parse_line(line: str) -> tuple[int, list[int], list[int]]:
    left, m_nums = line.split("|")
    card, w_nums = left.split(":")
    card = card.removeprefix("Card ")
    return int(card), [int(n) for n in w_nums.split()], [int(n) for n in m_nums.split()]


if __name__ == "__main__":
    # print(timeit(main, number=1))
    main()
