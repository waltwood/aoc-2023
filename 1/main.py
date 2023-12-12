# from timeit import timeit

NUM_STRS = [
    "one",
    "1",
    "two",
    "2",
    "three",
    "3",
    "four",
    "4",
    "five",
    "5",
    "six",
    "6",
    "seven",
    "7",
    "eight",
    "8",
    "nine",
    "9",
]


def main():
    total1 = 0
    total2 = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()

            val = parse_cal_val(line)
            # print(f"sum1: {total1} val: {val} ln: {line}")
            total1 = total1 + val

            val = parse_cal_val_with_text(line)
            print(f"sum2: {total2} val: {val} ln: {line}")
            total2 = total2 + val

    print(f"sum1: {total1}")
    print(f"sum2: {total2}")


def parse_cal_val(line: str) -> int:
    f_digit = ""
    l_digit = ""

    for c in line:
        if c.isdigit():
            f_digit: str = c
            break

    for c in line[::-1]:
        if c.isdigit():
            l_digit: str = c
            break

    return int(f_digit + l_digit)


def parse_cal_val_with_text(line: str) -> int:
    f_hits = {}
    l_hits = {}
    for ns_i, ns in enumerate(NUM_STRS):
        i = line.find(ns)  # look from beginning
        if i > -1:
            f_hits[i] = ns if ns.isdigit() else NUM_STRS[ns_i + 1]
        i = line.rfind(ns)  # look from end
        if i > -1:
            l_hits[i] = ns if ns.isdigit() else NUM_STRS[ns_i + 1]

    f_digit = sorted(f_hits.items())[0][1]
    l_digit = sorted(l_hits.items())[-1][1]

    return int(f_digit + l_digit)


if __name__ == "__main__":
    # print(timeit(main, number=1))
    main()
