import re

with open('input.txt', 'r') as file:
    ops = file.read()

reg1 = r"mul\(\d{1,3},\d{1,3}\)"
muls1 = re.findall(reg1, ops, re.MULTILINE)

part1 = sum(
    int(a) * int(b)
    for a, b
    in [re.findall(r"\d+", mul) for mul in muls1]
)
print(part1)
