import time

RENDERING_ON = True
def renderToOutput(data):
    if not RENDERING_ON:
        return
    outputString = ""
    for line in data:
        outputString += "".join(line) + "\n"

    file = open("day10/output.txt", "w")
    file.write(outputString)
    file.close()
    time.sleep(0.1)

#create data matrix
file = open("day10/data.txt")
data = file.read().split("\n")

for i in range(len(data)):
    data[i] = list(data[i])
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

def bfs(i, j, height):
    visited = set()
    queue = [(i, j, height)]
    score = 0

    while queue:
        x, y, height = queue.pop(0)
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if data[x][y] == 9:
            score += 1
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and data[nx][ny] == height + 1:
                queue.append((nx, ny, data[nx][ny]))

    return score

score_sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            score = bfs(i, j, 0)
            score_sum += score


print(f"Part 1: {score_sum}")

def dfs(i, j, height):
    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
        return 0

    if data[i][j] != height+1:
        return 0
    
    if data[i][j] == 9:
        return 1

    return dfs(i-1, j, data[i][j]) + dfs(i, j+1, data[i][j]) + dfs(i+1, j, data[i][j]) + dfs(i, j-1, data[i][j])

rating_sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            score = dfs(i, j, -1)
            rating_sum += score

print(f"Part 2: {rating_sum}")