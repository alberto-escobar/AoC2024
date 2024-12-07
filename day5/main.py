file = open("day5/rules.txt", "r")
rules = file.read().split("\n")
file.close()

file = open("day5/data.txt", "r")
data = file.read().split("\n")
file.close()

rule_map = {}

for rule in rules:
    rule = rule.split("|")
    X = int(rule[0])
    Y = int(rule[1])
    if X not in rule_map:
        rule_map[X] = []
    rule_map[X].append(Y)

for i in range(len(data)):
    data[i] = list(map(int, data[i].split(",")))

sum = 0
invalid_updates = []
for update in data:
    invalid_update_flag = False
    for i in range(len(update)):
        if i == len(update) - 1:
            break
        X = update[i]
        X_rules = rule_map[X]
        Ys = update[i+1:]
        for Y in Ys:
            if Y not in X_rules:
                invalid_update_flag = True
                break
        if invalid_update_flag:
            invalid_updates.append(update)
            break
    if not invalid_update_flag:
        sum += update[len(update)//2]

print(f"Part 1: {sum}")

def reorderPages(update):
    reordered_update = [-1]*len(update)
    for X in update:
        index = 0
        X_rules = rule_map[X]
        for Y in update:
            if X == Y:
                continue
            if Y in X_rules:
                index += 1
        reordered_update[len(update) - index - 1] = X
    return reordered_update
sum = 0
for update in invalid_updates:
    update = reorderPages(update)
    sum += update[len(update)//2]
print(f"Part 2: {sum}")
