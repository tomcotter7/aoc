disk_map = open("input.txt", "r").read().strip()

expanded_disk_map = []

id = 0
free_space = False
for char in disk_map:
    length = int(char)
    to_append = '.' if free_space else id
    expanded_disk_map += [to_append for _ in range(length)]
    if not free_space:
        id += 1
    free_space = not free_space

first = expanded_disk_map.index('.')
last = len(expanded_disk_map) - 1

while first < last:
    val = expanded_disk_map[last]
    expanded_disk_map[first] = val
    expanded_disk_map[last] = '.'

    first = expanded_disk_map[first:].index('.') + first
    last -= 1
    while expanded_disk_map[last] == '.':
        last -= 1

end = expanded_disk_map.index('.')
expanded_disk_map = expanded_disk_map[:end]

total = 0

for index, val in enumerate(expanded_disk_map):

    total += (index * int(val))

print(total)
