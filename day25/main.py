file = open("day25/data.txt")
data = file.read().split("\n\n")

keys = []
locks = []
for entry in data:
    entry = [list(row) for row in entry.split("\n")]
    if entry[0] == ["#", "#", "#", "#", "#"]:
        locks.append(entry)
    else:
        keys.append(entry)

keys_nums = []
locks_nums = []
for lock in locks:
    nums = [0, 0, 0, 0, 0]
    for i in range(len(lock[0])):
        for j in range(1, len(lock), 1):
            if lock[j][i] == "#":
                nums[i] += 1
    locks_nums.append(nums)

for key in keys:
    nums = [0, 0, 0, 0, 0]
    for i in range(len(key[0])):
        for j in range(len(key)):
            if j == len(key)-1:
                continue
            if key[j][i] == "#":
                nums[i] += 1
    keys_nums.append(nums)

def check_fit(lock, key):
    fit = [0, 0, 0, 0, 0]
    for i in range(len(lock)):
        fit[i] = lock[i] + key[i]
        if fit[i] > 5:
            return None
    return fit

sum = 0
pairs = {}
for key in keys_nums:
    for lock in locks_nums:
        if check_fit(lock, key):
            sum += 1
print(f"part 1: {sum}")

print(f"part 2: Merry Christmas!")