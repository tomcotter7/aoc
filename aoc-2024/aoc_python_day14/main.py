from robot import Robot
from functools import reduce
import re

FILENAME = "input.txt"
TIMESTEPS = 10403
BOARD_W = 101
BOARD_H = 103


def process_bot(data: str) -> Robot:
    p, v = data.split(" ", 1)
    p_x, p_y = p.split("=", 1)[1].split(",", 1)
    v_x, v_y = v.split("=", 1)[1].split(",", 1)

    fdata = {
        "pos_x": int(p_x),
        "pos_y": int(p_y),
        "vel_x": int(v_x),
        "vel_y": int(v_y),
        "board_w": BOARD_W,
        "board_h": BOARD_H,
    }

    return Robot(**fdata)


def print_board(robots: list[Robot], timestep: int) -> None:
    board = [["-" for _ in range(BOARD_W)] for _ in range(BOARD_H)]

    for robot in robots:
        if board[robot.pos_y][robot.pos_x] == "-":
            board[robot.pos_y][robot.pos_x] = 1
        else:
            board[robot.pos_y][robot.pos_x] += 1

    is_line = False
    is_pot = False
    for idx, row in enumerate(board):
        row = "".join([str(pos) for pos in row])
        is_line = re.match(r"\d{3,101}", row)
        if is_line:
            prev_row = "".join([str(pos) for pos in board[idx - 1]])
            is_pot = re.match(r"\d-\d", prev_row)
            if is_pot:
                break

    if is_line and is_pot:
        print(f"TIMESTEP: {timestep}")
        for row in board:
            row = "".join([str(pos) for pos in row])
            row_has_line = re.match(r"\d{3,101}", row)
            if row_has_line:
                print(f"\033[91m{row}\033[0m")
            else:
                print(row)


def main():
    bots = [
        process_bot(data) for data in open(FILENAME, "r").read().strip().splitlines()
    ]

    for t in range(TIMESTEPS):
        for bot in bots:
            bot.tick()
        print_board(bots, t)

    quadrants = [0 for _ in range(4)]

    for bot in bots:
        quadrant = bot.get_quadrant()
        if quadrant is not None:
            quadrants[quadrant] += 1

    print(reduce(lambda x, y: x * y, quadrants))


if __name__ == "__main__":
    main()
