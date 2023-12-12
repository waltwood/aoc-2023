import functools
import operator
from typing import Optional


def main():
    total1 = 0
    total2 = 0
    with open("input.txt", "r") as f:
        lines = [ln.strip() for ln in f]

    # load nums and check neighbors
    part_numbers = load_part_numbers(lines)

    for part_num, coords in part_numbers:
        is_part_num = False
        for r, c in coords:
            if check_neighbors(r, c, lines):
                is_part_num = True
                break

        if is_part_num:
            total1 += int(part_num)

        # print(f"{int(part_num)} {is_part_num} {coords} {total1}")

    gear_ratios = {}
    for part_num, coords in part_numbers:
        for r, c in coords:
            gear = check_neighbors_for_gear(r, c, lines)
            if gear:
                gear_ratios.setdefault(gear, []).append(int(part_num))
                break  # this might only work if each part has only one gear

    for gear, part_nums in gear_ratios.items():
        if len(part_nums) > 1:
            ratio = functools.reduce(operator.mul, part_nums)
            total2 += ratio
            # print(gear, part_nums, ratio)

    print(total1)
    print(total2)


def check_neighbors_for_gear(r: int, c: int, grid: list[str]) -> Optional[tuple]:
    neighbors = get_neighbors(r, c, grid)
    for i, n in enumerate(neighbors):
        if n and n == "*":
            # [ul, up, ur, left, right, dl, down, dr]
            if i == 0:
                return r - 1, c - 1
            if i == 1:
                return r - 1, c
            if i == 2:
                return r - 1, c + 1
            if i == 3:
                return r, c - 1
            if i == 4:
                return r, c + 1
            if i == 5:
                return r + 1, c - 1
            if i == 6:
                return r + 1, c
            if i == 7:
                return r + 1, c + 1
    return None


def check_neighbors(r: int, c: int, grid: [[]]) -> bool:
    neighbors = get_neighbors(r, c, grid)
    # print(grid[r][c], neighbors, end=" ")
    for n in neighbors:
        if n and (not n.isdigit() and not n == "."):
            return True
    return False


def load_part_numbers(lines: list) -> list:
    part_numbers = []
    for row, ln in enumerate(lines):
        num_s = ""
        coords = []
        for col, ch in enumerate(ln):
            if ch.isdigit():
                num_s = num_s + ch
                coords.append((row, col))
            else:
                if num_s:
                    part_numbers.append((num_s, coords))
                num_s = ""
                coords = []
        if num_s:  # last num in row
            part_numbers.append((num_s, coords))
    return part_numbers


def get_neighbors(r: int, c: int, grid: list[str]) -> list[str]:
    c_bound = len(grid[0]) - 1
    r_bound = len(grid) - 1
    up = None if r == 0 else grid[r - 1][c]
    down = None if r >= r_bound else grid[r + 1][c]
    left = None if c == 0 else grid[r][c - 1]
    right = None if c >= c_bound else grid[r][c + 1]
    # diagonals
    ul = None if not (up and left) else grid[r - 1][c - 1]
    ur = None if not (up and right) else grid[r - 1][c + 1]
    dl = None if not (down and left) else grid[r + 1][c - 1]
    dr = None if not (down and right) else grid[r + 1][c + 1]

    return [ul, up, ur, left, right, dl, down, dr]


if __name__ == "__main__":
    # print(timeit(main, number=1))
    main()
