file = open("day20/data.txt")
data = [list(row_string) for row_string in file.read().split("\n")]

start = None
end = None

for j in range(len(data)):
    for i in range(len(data)):
        if data[j][i] == "S":
            start = (i, j)
        elif data[j][i] == "E":
            end = (i, j)

def find_path(track, start, end):
    path = []
    visited = {}
    current = start
    count = 0
    while current != end:
        x, y = current
        path.append(current)
        visited[current] = count
        directions = [
            (x, y-1),
            (x+1, y),
            (x, y+1),
            (x-1, y)
        ]
        for direction in directions:
            nx, ny = direction
            if track[ny][nx] != "#" and direction not in visited:
                current = direction
                count += 1
                break
    path.append(current)
    visited[current] = count
    return path

def find_cheats(track, path, path_set, limit):
    cheats = []
    for position in path:
        x, y = position
        directions = [
            (0, -1),
            (+1, 0),
            (0, +1),
            (-1, 0)
        ]
        for direction in directions:
            dx, dy = direction
            #not a wall or in border, dont check
            if track[y+dy][x+dx] != "#" or x+dx == 0 or x+dx == len(track[0]) or y+dy == 0 or y+dy == len(track):
                continue
            #past wall is a path point in the future
            elif (x+(dx*2), y+(dy*2)) in path_set and path_set[(x+(dx*2), y+(dy*2))] > path_set[(x, y)]:
                time_saved = path_set[(x+(dx*2), y+(dy*2))] - path_set[position] - 2
                if time_saved < limit:
                    continue    
                cheats.append([position, (x+dx, y+dy), time_saved])
    return cheats

path = find_path(data, start, end)
path_with_counts = {}
for i in range(len(path)):
    path_with_counts[path[i]] = i

cheats = find_cheats(data, path, path_with_counts, 100)

print(f"part 1: {len(cheats)}")

def count_new_cheats(path, path_set, cheat_length, limit):
    count = 0
    for p1 in path:
        for p2 in path:
            x1, y1 = p1
            x2, y2 = p2
            m_dist = abs(x1 - x2) + abs(y1 - y2)
            if m_dist > cheat_length:
                continue
            time_saved = path_set[p2] - path_set[p1] - m_dist
            if time_saved < limit:
                continue
            count += 1
    return count
count = count_new_cheats(path, path_with_counts, 20, 100)
print(f"part 2: {count}")
