import time
file = open("day16/data.txt")
data = file.read().split("\n")

maze = []
for row in data:
    maze.append(list(row))

start = None
end = None
for j in range(len(maze)):
    for i in range(len(maze[j])):
        if maze[j][i] == "S":
            start = (i, j)
        if maze[j][i] == "E":
            end = (i, j)
        
queue = [[start, "E", 0, []]]
best_score = float("inf")
best_paths_tiles = set()
visited = {}
while queue:
    position, facing, current_score, path = queue.pop(0)
    x, y = position
    # important here is to check if you visited this spot and the current score is the same
    # as before. You you are checking just "<" your going to go in loooong loops.
    if (position, facing) in visited and visited[(position, facing)] <= current_score:
        continue
    
    visited[(position, facing)] = current_score

    if maze[y][x] == "E":
        if current_score < best_score:
            best_score = current_score
            best_paths_tiles.clear()
            best_paths_tiles.update(path)
            
        elif current_score == best_score:
            best_paths_tiles.update(path)
        continue

    path = set(path)
    path.add(position)
    path = list(path)
    if facing == "E":
        if maze[y][x+1]!="#":
            queue.append([(x+1, y), "E", current_score+1, path])
        queue.append([(x, y), "N", current_score+1000, path])
        queue.append([(x, y), "S", current_score+1000, path])
    elif facing == "N":
        if maze[y-1][x]!="#":
            queue.append([(x, y-1), "N", current_score+1, path])
        queue.append([(x, y), "W", current_score+1000, path])
        queue.append([(x, y), "E", current_score+1000, path])
    elif facing == "W":
        if maze[y][x-1]!="#":
            queue.append([(x-1, y), "W", current_score+1, path])
        queue.append([(x, y), "S", current_score+1000, path])
        queue.append([(x, y), "N", current_score+1000, path])
    elif facing == "S":
        if maze[y+1][x]!="#":
            queue.append([(x, y+1), "S", current_score+1, path])
        queue.append([(x, y), "E", current_score+1000, path])
        queue.append([(x, y), "W", current_score+1000, path])

print(f"Part 1: {best_score}")
print(f"Part 2: {len(best_paths_tiles)+1}")


# this was a tough problem to solve, this code 
# helped me figure out what was causing my algorithm 
# to mess up: https://tinyurl.com/2m838xb9
#
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠈⠙⠛⢷⣦⡀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣀⣤⠴⠶⠚⠛⠛⠛⠲⠾⢿⣟⠛⠻⠶⣤⣀⠀⠀⠙⣿⡀⠀⠀
# ⠀⠀⠀⠀⣰⠟⣱⢦⢍⢋⠈⡂⠀⠀⠀⠀⠀⠈⠛⣦⠀⠀⠙⠳⣦⡀⣸⡇⠀⠀
# ⠀⢀⣠⣤⣯⠤⠷⢦⣼⠈⢤⡅⠀⠀⠀⠀⠀⠀⠀⠘⠷⣄⠀⠀⢈⣿⡟⠀⠀⠀
# ⢀⡾⠁⠂⠀⠀⠀⠈⣿⠀⠘⠁⠀⠀⠀⠀⠀⢀⠆⠀⠀⣸⠀⢀⣿⡿⠀⠀⠀⠀
# ⣸⠃⠀⠀⠀⠀⠀⡜⢻⠀⢰⡀⠀⠒⠒⠀⣔⡁⠀⢀⠞⣽⣀⣾⡿⠁⠀⠀⠀⠀
# ⢿⡀⠄⠀⠀⠀⢠⣷⢆⠝⢫⡀⠀⠀⠀⢰⢏⠩⠍⠁⠀⡏⣹⣿⣅⠀⠀⠀⠀⠀
# ⠈⣻⣄⠀⠀⠀⢨⡿⠥⠄⣀⣹⠀⠀⠀⢸⡼⠀⠀⠀⡰⢰⣽⡿⣿⠇⠀⠀⠀⠀
# ⠀⠙⠻⣿⣿⣶⣻⠤⠤⣄⣀⠈⠑⠓⠒⠋⡇⣀⠄⣊⣴⣿⠞⣷⡇⠀⠀⠀⠀⠀
# ⠀⠀⠀⠈⠉⠻⣅⠀⢨⠀⠀⠉⢭⣽⣿⣉⣭⣴⣿⣿⣿⣇⠀⣿⣿⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢐⡏⠀⠀⡀⠀⠀⠀⠹⣯⠛⠛⠁⣸⣿⠷⣯⣳⣾⣿⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⣰⠿⡖⢺⣿⣿⣆⠀⠀⠈⢷⡀⣰⣿⠃⠀⠀⠙⠳⠾⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⢸⣏⣐⣷⠟⠁⠀⠙⣧⡀⠀⠈⢻⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⣨⣷⣤⠚⢉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠫⣡⢣⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣶⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#  PLEASE NO MORE 2D PUZZLES