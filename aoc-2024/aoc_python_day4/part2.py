ws = [list(line) for line in open("input.txt", "r").read().strip().split("\n")]


for row in ws:
    print(row)

def is_out_of_bounds(pos: tuple[int, int], ws: list[list[str]]) -> bool:

    if pos[0] < 0 or pos[0] > len(ws) -1 or pos[1] < 0 or pos[1] > len(ws[0]) -1:
        return True

    return False

def check_for_x_mas(pos, ws) -> int:

    if ws[pos[0]][pos[1]] != "A":
        return 0

    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    if any(is_out_of_bounds((pos[0] + direction[0], pos[1] + direction[1]), ws) for direction in directions):
        return 0

    tl = ws[pos[0] - 1][pos[1] - 1]
    tr = ws[pos[0] - 1][pos[1] + 1]
    bl = ws[pos[0] + 1][pos[1] - 1]
    br = ws[pos[0] + 1][pos[1] + 1]

    def valid_diagonal(l1, l2):
        return l1 == "M" and l2 == "S" or l1 == "S" and l2 == "M"

    if valid_diagonal(tl, br) and valid_diagonal(tr, bl):
        return 1

    return 0

total = 0
for i, row in enumerate(ws):
    for j, letter in enumerate(row):
        total += check_for_x_mas((i, j), ws)

print(total)
