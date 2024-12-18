def render(matrix):
    outputString = ""
    for line in matrix:
        outputString += "".join(line) + "\n"
    file = open("day18/output.txt", "w")
    file.write(outputString)
    file.close()

file = open("day18/data.txt")
data = file.read().split("\n")

SPACE_SIZE = 71
START = (0, 0)
END = (SPACE_SIZE-1, SPACE_SIZE-1)
SIMULATION_STOP = 1024

falling_bytes = []
for row in data:
    a = []
    row = row.split(",")
    for num in row:
        a.append(int(num))
    falling_bytes.append(a)



def simulate_falling(bytes, stop):
    matrix = []
    for _ in range(SPACE_SIZE):
        row = []
        for _ in range(SPACE_SIZE):
            row.append(".")
        matrix.append(row)

    for i in range(stop):
        byte = bytes[i]
        x, y = byte
        matrix[y][x] = "#"
    return matrix

def bfs(maze, start, end):
    edge = len(maze)
    queue = [[start, 0]]
    steps = float("inf")
    visited = set()
    while queue:
        postion, steps_taken = queue.pop(0)
        x, y = postion
        
        #out of bounds
        if x < 0 or x == edge or y < 0 or y == edge:
            continue
        
        #hit a wall
        if maze[y][x] == "#":
            continue
        
        #we have been here before
        if postion in visited:
            continue

        #we reach the end, YIPPE
        if postion == end:
            if steps_taken < steps:
                steps = steps_taken
            continue
        steps_taken = steps_taken+1
        visited.add(postion)
        n = [(x, y-1), steps_taken]
        e = [(x+1, y), steps_taken]
        s = [(x, y+1), steps_taken]
        w = [(x-1, y), steps_taken]
        queue.append(n)
        queue.append(e)
        queue.append(s)
        queue.append(w)
    return steps

space_at_1024 = simulate_falling(falling_bytes, 1024)
min_steps = bfs(space_at_1024, START, END)

print(f"part 1: {min_steps}")

low = 0
high = len(falling_bytes)-1
ans = None
previous = None
while True:
    middle = (high+low)//2
    middle2 = middle-1

    maze1 = simulate_falling(falling_bytes, middle)
    steps1 = bfs(maze1, START, END)
    maze2 = simulate_falling(falling_bytes, middle2)
    steps2 = bfs(maze2, START, END)
    
    if steps1 == float("inf"):
        if steps2 != float("inf"):
            ans = falling_bytes[middle-1]
            break
        
    if maze1 != float("inf"):
        low = middle

    if maze2 == float("inf"):
        high = middle

    if (middle, middle2) == previous:
        high -= 1
        low += 1
    previous = (middle, middle2)

print(f"part 2: {ans}")