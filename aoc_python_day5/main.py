file = open("input.txt", "r").read()

rules, updates = file.split("\n\n")
rules = rules.split("\n")

updates = updates.strip().split("\n")
rules = [rule.split("|") for rule in rules]

rule_dict = {}
for pre, post in rules:
    rule_dict[post] = rule_dict.get(post, []) + [pre]

# 75, 47, 61, 53, 29

# anything that 29 has to be before but is in the list, FAIL
# anything that 53 has to be before but is in the list, FAIL

valid_updates = []
invalid_updates = []

for update in updates:

    pages = update.split(",")
    valid = True
    for i, page in enumerate(pages):
        if page in rule_dict:
            for post in pages[i+1:]:
                if post in rule_dict[page]:
                    valid = False
                    break
        if not valid:
            break
    if valid:
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

total = 0
for vu in valid_updates:
    pages = vu.split(",")
    midpoint = int(pages[len(pages) // 2])
    total += midpoint

print("Part 1:")
print(total)

print("===============")


def check_validity(pages, rule_dict):
    for i, page in enumerate(pages):
        if page in rule_dict:
            for post in pages[i+1:]:
                if post in rule_dict[page]:
                    return False
    return True

new_valid_updates = []
for iu in invalid_updates:
    pages = iu.split(",")
    while not check_validity(pages, rule_dict):
        for i, page in enumerate(pages):
            if page in rule_dict:
                for j, post in enumerate(pages[i+1:]):
                    if post in rule_dict[page]:
                        value = pages.pop(i+j+1)
                        pages.insert(i, value)

    new_valid_updates.append(pages)


total = 0
for vu in new_valid_updates:
    pages = vu
    midpoint = int(pages[len(pages) // 2])
    total += midpoint

print("Part 2:")
print(total)








