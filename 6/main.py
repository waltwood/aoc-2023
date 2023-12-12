def main():
    file = "input.txt"
    # file = "sample.txt"
    with open(file, "r") as f:
        lines = list(filter(None, map(str.strip, f)))

    races = parse_lines(lines)

    print(solve_1(races))
    print(solve_2(races))


def solve_2(races: list[tuple[str, str]]) -> int:
    new_time, new_dist = "", ""
    for time, dist in races:
        new_time += time
        new_dist += dist

    return solve_1([(new_time, new_dist)])


def solve_1(races: list[tuple[str, str]]) -> int:
    solution = 1
    for time, dist in races:
        time, dist = int(time), int(dist)
        wins = 0
        # for t in range(int(time / 6), int(time / 2 + time / 3)):
        for t in range(1, time):
            sim_dist = t * (time - t)
            if sim_dist > dist:
                wins += 1
        solution *= wins
    return solution


def parse_lines(lines: list[str]):
    time_list = list(filter(None, lines[0].removeprefix("Time:").split(" ")))
    dist_list = list(filter(None, lines[1].removeprefix("Distance:").split(" ")))
    return list(zip(time_list, dist_list))


if __name__ == "__main__":
    # print(timeit(main, number=1))
    main()
