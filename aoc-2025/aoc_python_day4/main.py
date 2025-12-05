def part2():
    pass


def part1(grid: list[str], *, update: bool = False) -> int:
    check_sum = 0

    height = len(grid)
    width = len(grid[0])
    total_pos = height * width

    for idx in range(total_pos):
        x, y = divmod(idx, width)

        if grid[x][y] == "@":
            x_nbours = grid[max(x - 1, 0) : min(x + 2, height)]
            neighbours = "".join(
                [row[max(y - 1, 0) : min(y + 2, width)] for row in x_nbours]
            )

            if sum(1 for elem in neighbours if elem == "@") < 5:
                check_sum += 1

    return check_sum


def main():
    data = open("input.txt", "r").read()
    grid = [row for row in data.splitlines()]

    print(part1(grid))


if __name__ == "__main__":
    main()
