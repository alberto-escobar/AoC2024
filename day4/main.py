file = open("day4\data.txt", "r")
data = file.read().split("\n")
file.close()

for i in range(len(data)):
    data[i] = list(data[i])

#part 1
directions = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1]
]

def dfs(x, y, direction, word):
    if len(word) == 0:
        return True
    
    if x < 0 or y < 0:
        return False
    if x >= len(data[0]) or y >= len(data):
        return False
    if data[x][y] != word[0]:
        return False
    word.pop(0)
    return dfs(x + direction[0], y + direction[1], direction, word)

count = 0
for row in range(len(data)):
    for column in range(len(data[row])):
        for direction in directions:
            xmas = ["X", "M", "A", "S"]
            if dfs(column, row, direction, xmas):
                count += 1
print(f"Part 1: {count}")

#part 2
def checkX(row, column):
    flag1 = False
    if data[row-1][column-1] == "M" and data[row+1][column+1] == "S":
        flag1 = True
    if data[row-1][column-1] == "S" and data[row+1][column+1] == "M":
        flag1 = True
    flag2 = False
    if data[row+1][column-1] == "M" and data[row-1][column+1] == "S":
        flag2 = True
    if data[row+1][column-1] == "S" and data[row+-1][column+1] == "M":
        flag2 = True
    return flag1 and flag2

count = 0
for row in range(1 , len(data)-1):
    for column in range(1, len(data[row])-1):
        if data[row][column] == "A":
            if checkX(row, column):
                count += 1

print(f"Part 2: {count}")
