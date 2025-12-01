ws = [list(line) for line in open("input.txt", "r").read().strip().split("\n")]

letters = {
    "X": "M",
    "M": "A",
    "A": "S",
}

current_letter = "X"
last_letter = "S"

for row in ws:
    print(row)


def is_out_of_bounds(pos: tuple[int, int], ws: list[list[str]]) -> bool:
    if pos[0] < 0 or pos[0] > len(ws) - 1 or pos[1] < 0 or pos[1] > len(ws[0]) - 1:
        return True

    return False


def next_letter_is_surrounding(
    ws: list[list[str]],
    letter: str,
    current_pos: tuple[int, int],
    direction: tuple[int, int],
) -> int:
    next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

    if is_out_of_bounds(next_pos, ws):
        return 0

    found_letter = ws[next_pos[0]][next_pos[1]]
    if found_letter == letter:
        if letter == last_letter:
            return 1
        else:
            return next_letter_is_surrounding(
                ws, letters[found_letter], next_pos, direction
            )

    return 0


directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

total = 0

for i, row in enumerate(ws):
    for j, letter in enumerate(row):
        if letter == "X":
            for direction in directions:
                if next_letter_is_surrounding(ws, letters[letter], (i, j), direction):
                    total += 1


print(total)
