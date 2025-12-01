import time

DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

TURN = {"^": ">", ">": "v", "v": "<", "<": "^"}

map = open("test.txt").readlines()
map = [list(line.strip()) for line in map]

current = (0, 0)
direction = "^"
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] in DIRECTIONS:
            current = (i, j)
            direction = map[i][j]
            break
    if current != (0, 0):
        break


def move(current, direction, map):
    new_pos = (
        current[0] + DIRECTIONS[direction][0],
        current[1] + DIRECTIONS[direction][1],
    )

    print(new_pos)

    if new_pos[0] < 0 or new_pos[1] < 0:
        raise IndexError

    if new_pos[0] >= len(map) or new_pos[1] >= len(map[0]):
        raise IndexError

    if map[new_pos[0]][new_pos[1]] == "#":
        new_direction = TURN[direction]
        map[current[0]][current[1]] = new_direction
        return move(current, new_direction, map)
    else:
        map[current[0]][current[1]] = "X"
        map[new_pos[0]][new_pos[1]] = direction
        return new_pos, direction, map


while True:
    try:
        current, direction, map = move(current, direction, map)
        size = 10
        # subset_of_map = [
        #     line[current[1] - size : current[1] + size + 1]
        #     for line in map[current[0] - size : current[0] + size + 1]
        # ]
        print("\n".join(["".join(line) for line in map]))
        print("=" * 20)
        time.sleep(1)
    except IndexError:
        map[current[0]][current[1]] = "X"
        break


total = 0
for line in map:
    for pos in line:
        if pos == "X":
            total += 1

print(total)

print("\n".join(["".join(line) for line in map]))
