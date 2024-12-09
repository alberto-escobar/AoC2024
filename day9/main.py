import time

#load data
file = open("day9/data.txt")
data = file.read()

disk_map = data

block_map = []
id = 0
for i in range(len(disk_map)):
    if i%2 == 0:
        for _ in range(int(disk_map[i])):
            block_map.append(id)
        id += 1
    elif i%2 == 1:
        for _ in range(int(disk_map[i])):
            block_map.append(".")

right = len(block_map)-1
left = 0
while right > left:
    while block_map[right] == ".":
        right -= 1

    while block_map[left] != ".":
        left += 1

    while block_map[right] != "." and block_map[left] == ".":
        block_map[left] = block_map[right]
        block_map[right] = "."
        left += 1
        right -= 1

sum = 0 
for i in range(len(block_map)):
    if block_map[i] == ".":
        break
    sum += block_map[i]*i
    
print(f"Part 1: {sum}")


block_map = []
id = 0
for i in range(len(disk_map)):
    if i%2 == 0:
        block_map.append([id, int(disk_map[i])])
        id += 1
    elif i%2 == 1:
        block_map.append([".", int(disk_map[i])])


def findFreeSpace(length, limit):
    left = 0
    while left < limit:
        #find first free space
        while block_map[left][0] != ".":
            left += 1
        
        #find length of space
        free_length = block_map[left][1]
        if free_length >= length:
            return left
        
        left += 1
    return None




right = len(block_map)-1
current_id = id-1
while current_id != 0:
    while block_map[right][0] != current_id:
        right -= 1

    length = block_map[right][1]
    left = findFreeSpace(length, right)

    if left != None:
        block_map[left][1] -= length
        temp = block_map[right].copy()
        block_map[right][0] = "."
        block_map.insert(left, temp)
        
    current_id -= 1

sum = 0
block_number = 0
for i in range(len(block_map)):
    block_id = block_map[i][0]
    num_of_blocks = block_map[i][1]
    if block_id == ".":
        block_number += num_of_blocks
        continue
    for i in range(num_of_blocks):
        sum += block_id*block_number
        block_number += 1
        

print(f"Part 2: {sum}")