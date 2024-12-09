memory = open("input.txt", "r").read().strip()
disk_map = []

id = 0
free_space = False
for char in memory:
    length = int(char)
    to_append = '.' if free_space else id
    disk_map += [to_append for _ in range(length)]
    if not free_space:
        id += 1
    free_space = not free_space


free_memory = []
used_memory = []
free = False
idx = 0

for char in memory:
    if free:
        free_memory.append(int(char))
    else:
        used_memory.append((idx, int(char)))
        idx += 1
    free = not free

# print(free_memory)
# print(used_memory)

def is_space_to_left(idx, size) -> int:

    for i, fs in enumerate(free_memory[:idx]):
        if fs >= size:
            return i

    return -1

def insert_at_left_most(disk_map, value):
    csp = disk_map.index('.')
    try:
        while True:
            if disk_map[csp:csp+value[1]].count('.') >= value[1]:
                disk_map = ['.' if x == '.' or x == value[0] else x for x in disk_map]
                for i in range(value[1]):
                    disk_map[csp + i] = value[0]
                return disk_map
            csp = disk_map.index('.', csp + 1)
    except ValueError:
        return disk_map


for idx in range(len(used_memory) - 1, -1, -1):
    value = used_memory[idx]
    size = value[1]
    new_pos = is_space_to_left(idx, size)
    if new_pos != -1:
        disk_map = insert_at_left_most(disk_map, value)

    free_memory[new_pos] -= size


total = 0

for index, val in enumerate(disk_map):
    if val == '.':
        continue
    total += (index * int(val))

print(total)
