Map = list[list[int]]
Pos = tuple[int, int]

directions: list[Pos] = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
]


def find_all(topo_map: Map, number: int = 9) -> list[tuple[Pos, Pos]]:
    positions = []

    for row in range(len(topo_map)):
        for col in range(len(topo_map[row])):
            if topo_map[row][col] == number:
                positions.append(((row, col), (row, col)))

    return positions


def add_pos(x: Pos, y: Pos) -> Pos:
    return x[0] + y[0], x[1] + y[1]


def is_valid_pos(p: Pos, topo_map: Map) -> bool:
    if p[0] < 0 or p[0] >= len(topo_map) or p[1] < 0 or p[1] >= len(topo_map[0]):
        return False

    return True


def read_input(filename: str) -> Map:
    data = open(filename).read().strip().split("\n")
    topo_map = []
    for d in data:
        row = []
        for char in d:
            try:
                row.append(int(char))
            except Exception:
                row.append(-1)
        topo_map.append(row)
    return topo_map


def find_neighbors(
    topo_map: Map, sources: list[tuple[Pos, Pos]], target: int
) -> list[tuple[Pos, Pos]]:
    targets = []

    for source in sources:
        for dire in directions:
            new_pos = add_pos(source[1], dire)
            if is_valid_pos(new_pos, topo_map):
                if topo_map[new_pos[0]][new_pos[1]] == target:
                    targets.append((source[0], new_pos))

    return targets


def main():
    topo_map = read_input("input.txt")

    sources = find_all(topo_map, 9)
    target = 8

    while target >= 0:
        sources = find_neighbors(topo_map, sources, target)
        # sources = list(set(sources))
        target -= 1

    print(len(sources))


if __name__ == "__main__":
    main()
