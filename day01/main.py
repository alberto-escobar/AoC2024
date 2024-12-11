file = open("day01\data.txt", "r")
data = file.read().split("\n")
file.close()

#part 1
list1 = []
list2 = []
for entry in data:
    pair = entry.split()
    list1.append(int(pair[0]))
    list2.append(int(pair[1]))

list1.sort()
list2.sort()
diff_sum = 0
for i in range(len(list1)):
    diff_sum += abs(list1[i] - list2[i])

print(f"Part 1 answer: {diff_sum}")

#part 2
map1 = {}
map2 = {}
list1 = []
list2 = []
for entry in data:
    pair = entry.split()
    if int(pair[0]) in map1:
        map1[int(pair[0])] += 1
    else:
        map1[int(pair[0])] = 1
    if int(pair[1]) in map2:
        map2[int(pair[1])] += 1
    else:
        map2[int(pair[1])] = 1

similarity_score = 0
for key1 in map1.keys():
    similarity_score += key1 * map2.get(key1, 0)
print(f"Part 2 answer: {similarity_score}")
