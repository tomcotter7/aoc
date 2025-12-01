def part1():

    stones = open("input.txt", "r").read().split()
    stones = [int(s) for s in stones]

    def apply_step(stones: list[int]):
        new_stones = []
        for stone in stones:
            s_stone = str(stone)
            length = len(s_stone)
            if stone == 0:
                new_stones.append(1)
            elif length % 2 == 0:
                new_stones.append(int(s_stone[:length//2]))
                new_stones.append(int(s_stone[length//2:]))
            else:
                new_stones.append(stone * 2024)

        return new_stones


    N_STEPS = 25

    for _ in range(N_STEPS):
        stones = apply_step(stones)

    print(len(stones))

def part2():

    stones = open("test.txt", "r").read().split()

    stones = [int(s) for s in stones]

    prev = {}

    def apply_steps(stone: int, n: int):

        if n == 0:
            return 1
        
        if (stone, n) in prev:
            return prev[(stone, n)]

        s_stone = str(stone)
        length = len(s_stone)
        if stone == 0:
            result = apply_steps(1, n - 1)
            prev[(stone, n)] = result
            return result
        elif length % 2 == 0:
            left = apply_steps(int(s_stone[:length//2]), n - 1)
            right = apply_steps(int(s_stone[length//2:]), n - 1)
            prev[(stone, n)] = left + right
            return left + right
        else:
            result = apply_steps(stone * 2024, n - 1)
            prev[(stone, n)] = result
            return result
    
    N_STEPS = 25
    total = 0
    for stone in stones:
        total += apply_steps(stone, N_STEPS)

    print(total)

part2()
