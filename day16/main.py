import time
#create data matrix
file = open("day16/data.txt")
data = file.read().split("\n")

maze = []
for row in data:
    maze.append(list(row))

start = None
end = None
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == "S":
            start = (x, y)
        elif maze[y][x] == "E":
            end = (x, y)

initial_state = [start, "E", 0, None]
queue = []
previous_positions = {}
queue.append(initial_state)
visited = {}
best_score = float("inf")
while len(queue) != 0:
    state = queue.pop(0)
    position, facing, current_score, previous = state
    x, y = position

    #base case, wall
    if maze[y][x] == "#":
        continue

    #base case, already visited using less optimal path
    if (x, y) in visited and visited[(x, y)] <= current_score:
        continue

    best_current_score = visited.get((x, y), float("inf"))
    if current_score < best_current_score:
        previous_positions[position] = []
        previous_positions[position].append(previous)
    elif current_score == best_score and previous not in previous_positions[position]:
        previous_positions[position].append(previous)
    #base case, exit 
    if maze[y][x] == "E":
        best_score = min(current_score,best_score)
        visited[(x, y)] = best_score
        continue
    visited[(x, y)] = current_score

    if facing == "E":
        queue.append([(x+1, y), "E", current_score+1, position])
        queue.append([(x, y-1), "N", current_score+1001, position])
        queue.append([(x, y+1), "S", current_score+1001, position])
    elif facing == "N":
        queue.append([(x, y-1), "N", current_score+1, position])
        queue.append([(x-1, y), "W", current_score+1001, position])
        queue.append([(x+1, y), "E", current_score+1001, position])
    elif facing == "W":
        queue.append([(x-1, y), "W", current_score+1, position])
        queue.append([(x, y+1), "S", current_score+1001, position])
        queue.append([(x, y-1), "N", current_score+1001, position])
    elif facing == "S":
        queue.append([(x, y+1), "S", current_score+1, position])
        queue.append([(x+1, y), "E", current_score+1001, position])
        queue.append([(x-1, y), "W", current_score+1001, position])


print(f"Part 1: {best_score}")

queue = []
s = set()
queue.append(end)
while queue:
    position = queue.pop(0)
    print(position)
    s.add(position)
    if position == start:
        continue
    previous = previous_positions[position]
    for p in previous:
        queue.append(p)
print(previous_positions)