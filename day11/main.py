import time

#create data matrix
file = open("day11/data.txt")
data = file.read()
data = data.split()


for i in range(len(data)):
    data[i] = int(data[i])

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            string = str(stone)
            half_point = len(string)//2
            new_stone1 = int(string[:half_point])
            new_stone2 = int(string[half_point:])
            new_stones.append(new_stone1)
            new_stones.append(new_stone2)
            continue
        new_stones.append(stone*2024)
    return new_stones

stones = data.copy()
for i in range(25):
    stones = blink(stones)
    
print(f"Part 1: {len(stones)}")

stones = {}

for stone in data:
    if stone not in stones:
        stones[stone] = 0
    stones[stone] += 1

def change_stone(stone):
    if stone == 0:
        return[1]
    if len(str(stone)) % 2 == 0:
        string = str(stone)
        half_point = len(string)//2
        new_stone1 = int(string[:half_point])
        new_stone2 = int(string[half_point:])
        return [new_stone1, new_stone2]
    return [stone*2024]

def blink(stones):
    new_stones = {}
    for stone,count in stones.items():
        for new_stone in change_stone(stone):
            if new_stone not in new_stones:
                new_stones[new_stone] = 0
            new_stones[new_stone] += count
    return new_stones

for _ in range(75):
    stones = blink(stones)

sum = 0
for count in stones.values():
    sum += count

print(f"Part 2: {sum}")