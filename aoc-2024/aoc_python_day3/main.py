import re


def ipt_value(filename: str) -> str:
    file = open(filename, "r").read()
    return file


def part1(ipt: str) -> int:
    return sum(
        int(m.group(1)) * int(m.group(2))
        for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", ipt)
    )


def part2(ipt: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))"

    total = 0
    do = True
    for m in re.finditer(pattern, ipt):
        if "don't()" in str(m.group(3)):
            do = False
        elif "do()" in str(m.group(4)):
            do = True
        else:
            if do and m.group(1) and m.group(2):
                total += int(m.group(1)) * int(m.group(2))

    return total


print(part2(ipt_value("input.txt")))
