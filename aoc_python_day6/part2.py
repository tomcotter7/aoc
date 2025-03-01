import time
import copy

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

DIRECTIONS: dict[str, tuple[int, int]] = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}
DIFF = {UP: 1, DOWN: -1, LEFT: 1, RIGHT: -1}
TURN = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}

debug = False


def is_obstacle(char: str) -> bool:
    if char == "#" or char == "O":
        return True

    return False


board = open("input.txt").readlines()
board = [list(line.strip()) for line in board]


current = (0, 0)
direction = UP
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] in DIRECTIONS:
            current = (i, j)
            direction = board[i][j]
            break
    if current != (0, 0):
        break

nboard = [[("", "", "", "") for _ in range(len(board[i]))] for i in range(len(board))]
for i in range(len(board)):
    for j in range(len(board[i])):
        nboard[i][j] = (board[i][j], board[i][j], board[i][j], board[i][j])


def pad(string: str, padding: int) -> str:
    diff = padding - len(string)
    return string + ("_" * diff)


def print_board(board: list[list[str]]):
    print("\n".join([" ".join([pad(char, 4) for char in line]) for line in board]))


def find_next_obstacle(row_or_col: list[str], pos: int, direction: str) -> int | None:
    if direction == RIGHT or direction == DOWN:
        if debug:
            print(row_or_col[pos + 1 :])
        for i in range(len(row_or_col[pos + 1 :])):
            if is_obstacle(row_or_col[i + pos + 1]):
                return i + pos + 1

    elif direction == LEFT or direction == UP:
        if debug:
            print("find_next_obstacle:", row_or_col[:pos])
        for i in range(len(row_or_col[:pos]), -1, -1):
            if is_obstacle(row_or_col[i]):
                return i

    return None


def find_tail(row_or_col: list[str], pos: int, direction: str) -> bool:
    if debug:
        print(row_or_col, pos, direction)
    if direction == RIGHT or direction == DOWN:
        if debug:
            print(row_or_col[pos + 1 :], direction)
        for i in range(len(row_or_col[pos + 1 :])):
            if is_obstacle(row_or_col[i + pos + 1]):
                return False
            elif direction in row_or_col[i + pos + 1]:
                return True

    elif direction == LEFT or direction == UP:
        if debug:
            print("find_tail:", row_or_col[:pos])
        for i in range(len(row_or_col[:pos]), -1, -1):
            if is_obstacle(row_or_col[i]):
                return False
            elif direction in row_or_col[i]:
                return True
    return False


def check_for_infinite_loop(
    current: tuple[int, int],
    direction: str,
    board: list[list[str]],
) -> bool:
    if debug:
        print_board(board)
        print(direction)
    new_direction = TURN[direction]

    row_idx = current[0]
    col_idx = current[1]
    if new_direction == LEFT or new_direction == RIGHT:
        row = board[row_idx]
        if find_tail(row, col_idx, new_direction):
            if debug:
                print(f"Found tail in {new_direction} from {current}")
            return True

        elif (obs_idx := find_next_obstacle(row, col_idx, new_direction)) is not None:
            turn_pos = (row_idx, obs_idx + DIFF[new_direction])
            while current != turn_pos:
                current, _, board = move(current, new_direction, board)
            if debug:
                print(f"Found obstacle in {new_direction} from {current}")
            return check_for_infinite_loop(
                (row_idx, obs_idx + DIFF[new_direction]), new_direction, board
            )

    else:
        col = [board[i][col_idx] for i in range(len(board))]

        if find_tail(col, row_idx, new_direction):
            if debug:
                print(f"Found tail in {new_direction} from {current}")
            return True

        elif (obs_idx := find_next_obstacle(col, row_idx, new_direction)) is not None:
            if debug:
                print(f"Found obstacle in {new_direction} from {current}")
            turn_pos = (obs_idx + DIFF[new_direction], col_idx)
            while current != turn_pos:
                current, _, board = move(current, new_direction, board)
            return check_for_infinite_loop(
                (obs_idx + DIFF[new_direction], col_idx), new_direction, board
            )

    return False


def move(
    current: tuple[int, int], direction: str, board: list[list[str]]
) -> tuple[tuple[int, int], str, list[list[str]]]:
    new_pos = (
        current[0] + DIRECTIONS[direction][0],
        current[1] + DIRECTIONS[direction][1],
    )

    if new_pos[0] < 0 or new_pos[1] < 0:
        raise IndexError

    if new_pos[0] >= len(board) or new_pos[1] >= len(board[0]):
        raise IndexError

    if is_obstacle(board[new_pos[0]][new_pos[1]]):
        new_direction = TURN[direction]
        board[current[0]][current[1]] = new_direction
        return current, new_direction, board
    else:
        # board[current[0]][current[1]] = direction
        # board[new_pos[0]][new_pos[1]] = direction
        if board[current[0]][current[1]] == ".":
            board[current[0]][current[1]] = direction
        elif direction not in board[current[0]][current[1]]:
            board[current[0]][current[1]] = board[current[0]][current[1]] + direction
        if board[new_pos[0]][new_pos[1]] == ".":
            board[new_pos[0]][new_pos[1]] = direction
        elif direction not in board[new_pos[0]][new_pos[1]]:
            board[new_pos[0]][new_pos[1]] = board[new_pos[0]][new_pos[1]] + direction
        return new_pos, direction, board


total = 0

while True:
    try:
        cboard = copy.deepcopy(board)
        obstacle_pos = (
            current[0] + DIRECTIONS[direction][0],
            current[1] + DIRECTIONS[direction][1],
        )

        if cboard[obstacle_pos[0]][obstacle_pos[1]] == ".":
            cboard[obstacle_pos[0]][obstacle_pos[1]] = "O"
            if check_for_infinite_loop(current, direction, cboard):
                if debug:
                    print(
                        f"Infinite loop can be made with obstacle placed at {obstacle_pos}"
                    )
                    print_board(cboard)

                total += 1
                # cont = input("Continue: (y/n)").lower()
        current, direction, board = move(current, direction, board)
        size = 10
        # subset_of_map = [
        #     line[current[1] - size : current[1] + size + 1]
        #     for line in map[current[0] - size : current[0] + size + 1]
        # ]
        # print("=" * 20)
        # print("\n".join(["".join(line) for line in board]))
        # time.sleep(1)
    except IndexError:
        board[current[0]][current[1]] = "X"
        break

print(total)

# total = 0
# for line in board:
#     for pos in line:
#         if pos == "X":
#             total += 1
# print("\n".join(["".join(line) for line in board]))
