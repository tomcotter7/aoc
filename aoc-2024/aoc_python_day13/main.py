import re

games = open("input.txt", "r").read().split("\n\n")

total = 0

for game in games:

    rows = game.split("\n")

    button_pattern = re.compile(r"Button [A,B]{1}: X\+(\d+), Y\+(\d+)")
    prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
    button_a = button_pattern.search(rows[0])
    button_b = button_pattern.search(rows[1])
    prize = prize_pattern.search(rows[2])

    ba_x = int(button_a.group(1))
    ba_y = int(button_a.group(2))

    bb_x = int(button_b.group(1))
    bb_y = int(button_b.group(2))

    p_x = int(prize.group(1)) + 10000000000000
    p_y = int(prize.group(2)) + 10000000000000

    # (?_a * ba_x) + (?_b * bb_x) = p_x
    # (?_a * ba_y) + (?_b * bb_y) = p_y

    # ?_a = (p_x - (?_b * bb_x)) / (ba_x)

    # (((p_x - (?_b * bb_x)) / (ba_x)) * ba_y) + (?_b * bb_y) = p_y

    # (((p_x * ba_y) - (bb_x * ba_y * ?_b)) / ba_x) + (bb_y * ?_b) = p_y

    # (p_x * ba_y) - (bb_x * ba_y * ?_b) + (ba_x * bb_y * ?_b) = (ba_x * p_y)

    # (ba_x * bb_y * ?_b) - (bb_x * ba_y * ?_b) = (ba_x * p_y) - (ba_y * p_x)
     
    # ((ba_x * bb_y) - (bb_x * ba_y)) * ?_b = (ba_x * p_y) - (ba_y * p_x)

    unknown_b = ((ba_x * p_y) - (ba_y * p_x)) / ((ba_x * bb_y) - (bb_x * ba_y))
    unknown_a = (p_x - (unknown_b * bb_x)) / ba_x


    if int(unknown_b) == unknown_b and int(unknown_a) == unknown_a:

        print((3 * unknown_a) + unknown_b)

        total += ((3 * unknown_a) + unknown_b)

print(total)      
