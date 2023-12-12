import sys


def main():
    file = "input.txt"
    # file = "sample.txt"
    with open(file, "r") as f:
        lines = list(filter(None, map(str.strip, f)))

    seeds, maps = parse_lines(lines)
    funcs = populate_func_maps(maps)

    print(solve_1(seeds, funcs))
    print(solve_2(seeds, funcs))


def solve_2(seeds: list, funcs: dict) -> int:
    seed_ranges_in = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]  # fmt:skip
    solution = sys.maxsize
    for start, size in seed_ranges_in:
        seed_ranges = [(start, start + size - 1)]  # list for adding leftovers
        for map_name, func_list in funcs.items():
            seed_ranges = find_loc_for_seed_range(seed_ranges, func_list)
        # find the lowest result
        seed_ranges.sort()
        low_result = seed_ranges[0][0]
        solution = low_result if low_result < solution else solution

    return solution


def find_loc_for_seed_range(seed_ranges: list[tuple[int, int]], func_list: list) -> list[tuple[int, int]]:
    result_ranges = []
    for this_seed_range in seed_ranges:
        for func in func_list:
            f_range, f = func
            # find intersection with upper leftovers a.k.a rightovers
            r, leftovers, rightovers = intersection(this_seed_range, f_range)
            if rightovers:
                seed_ranges.append(rightovers)
            # apply f() to range bounds
            if r:
                result_ranges.append((f(r.start), f(r.stop)))
                break
    return result_ranges if result_ranges else seed_ranges


def intersection(r1: tuple, r2: tuple) -> (range, tuple[int, int], tuple[int, int]):
    r = range(max(r1[0], r2[0]), min(r1[1], r2[1]))
    leftovers = None
    rightovers = None
    if r or r.start == r.stop:
        leftovers = (r1[0], r.start - 1) if r.start > r1[0] else None
        rightovers = (r.stop + 1, r1[1]) if r1[1] > r.stop else None
    return r, leftovers, rightovers


def solve_1(seeds: list, funcs: dict) -> int:
    solution = sys.maxsize
    for seed in seeds:
        loc = seed
        for map_name, func_list in funcs.items():
            loc = find_loc_for_seed(loc, func_list)
        solution = loc if loc < solution else solution

    return solution


def find_loc_for_seed(seed: int, func_list: list) -> int:
    # evaluate map start and end
    m_start, m_end = func_list[0][0][0], func_list[-1][0][1]
    if not m_start <= seed <= m_end:
        return seed

    for func in func_list:
        (start, end), f = func
        # if seed between start and end apply f()
        if start <= seed <= end:
            return f(seed)
    return seed


def populate_func_maps(maps: dict) -> dict:
    func_maps = {}
    for map_name, sets in maps.items():
        func_maps[map_name] = []
        for dest, src, size in sets:
            f_range = src, src + size - 1
            # location = seed + ((src - dest) * -1)
            func_maps[map_name].append([f_range, lambda x, s=src, d=dest: x + ((s - d) * -1)])
        func_maps[map_name].sort()
    return func_maps


def parse_lines(lines: list[str]):
    seeds = []
    maps = {}
    map_name = ""
    for line in lines:
        if line.startswith("seeds: "):
            seeds = list(map(int, lines[0].removeprefix("seeds: ").split(" ")))
        if ":" in line:
            map_name = line.split(" ")[0]
        else:
            maps.setdefault(map_name, []).append(tuple(map(int, line.split(" "))))

    return seeds, maps


if __name__ == "__main__":
    # print(timeit(main, number=1))
    main()
