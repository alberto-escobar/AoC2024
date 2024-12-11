import time

#rendering function so I can view how data updates on the file while code runs
#handles converting matrix into printabe string
RENDERING_ON = False
def renderToOutput(data):
    if not RENDERING_ON:
        return
    outputString = ""
    for line in data:
        outputString += "".join(line) + "\n"

    file = open("day6/output.txt", "w")
    file.write(outputString)
    file.close()
    time.sleep(0.01)

#create data matrix
file = open("day6/data.txt")
data = file.read().split("\n")

for i in range(len(data)):
    data[i] = list(data[i])

#find start position
rows = len(data)
cols = len(data[0])
start = [0,0]
for row in range(rows):
    for col in range(cols):
        if data[row][col] == "^":
            start = [row, col]

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

current = start
i = 0
visited = set()
while True:
    next_row = current[0] + directions[i%4][0]
    next_col = current[1] + directions[i%4][1]

    #out of map check
    if next_row < 0 or next_row >= rows:
        visited.add(tuple(current))
        data[current[0]][current[1]] = "X"
        break
    if next_col < 0 or next_col >= cols:
        visited.add(tuple(current))
        data[current[0]][current[1]] = "X"
        break

    #obstacle check
    if data[next_row][next_col] == "#":
        i += 1
        continue

    #move forward
    visited.add(tuple(current))
    data[current[0]][current[1]] = "X"
    current = [next_row, next_col]
    data[current[0]][current[1]] = "^" 
    renderToOutput(data)

renderToOutput(data)
print(f"part 1: {len(visited)}")

def patrol(area):
    current = [0,0]
    for row in range(rows):
        for col in range(cols):
            if area[row][col] == "^":
                current = [row, col]
    steps = 0
    i = 0
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
    while True:
        if steps > rows*cols:
            
            return 0
        
        next_row = current[0] + directions[i%4][0]
        next_col = current[1] + directions[i%4][1]
        #out of map check
        if next_row < 0 or next_row >= rows:
            area[current[0]][current[1]] = "X"
            return 1
        if next_col < 0 or next_col >= cols:
            area[current[0]][current[1]] = "X"
            return 1

        #obstacle check
        if area[next_row][next_col] == "#":
            i += 1
            continue

        #move forward
        steps += 1
        area[current[0]][current[1]] = "X"
        current = [next_row, next_col]
        area[current[0]][current[1]] = "^" 
        renderToOutput(area)

sum = 0
iteration = 1
for potential_spot in visited:
    #print(f"{iteration}/{len(visited)}")
    iteration += 1
    file = open("day6/data.txt")
    data = file.read().split("\n")
    for i in range(len(data)):
        data[i] = list(data[i])
    data[potential_spot[0]][potential_spot[1]] = "#"
    if not patrol(data):
        sum += 1
print(f"part 2: {sum}")
