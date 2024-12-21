file = open("day20/data.txt")
data = [list(row_string) for row_string in file.read().split("\n")]
keypad1 = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
]
keypad2 = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]
keypad3 = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]
def bfs(area, start, end_pad):
    queue=[(start, [], [])]
    min_paths = []
    min_steps = float("inf")
    while queue:
        position, path, visited = queue.pop(0)
        x, y = position 
        if x < 0 or x >= len(area[0]) or y < 0 or y >= len(area):
            continue
        curr_pad = area[y][x]
        if  curr_pad == None:
            continue
        if curr_pad in visited:
            continue
        if curr_pad == end_pad:
            path = path+['A']
            if len(path) < min_steps:
                min_steps = len(path)
            if len(path) == min_steps:
                min_paths.append("".join(path))

            continue
        visited = visited + [curr_pad]
        queue.append(((x, y+1),path+['v'], visited))
        queue.append(((x-1, y),path+['<'], visited))
        queue.append(((x, y-1),path+['^'], visited))
        queue.append(((x+1, y),path+['>'], visited))
       
    return min_paths




def find_shortest_paths(keypad, string, start_pad):
    pad_map = {}
    for j in range(len(keypad)):
        for i in range(len(keypad[j])):
            pad = keypad[j][i]
            pad_map[pad] = (i,j)
    paths = None
    prev = start_pad
    for c in string:
        current = pad_map[prev]
        if not paths:
            paths = bfs(keypad, current, c)
        else:
            new_paths = bfs(keypad, current, c)
            temp = []
            for path in paths:
                for new_path in new_paths:
                    temp.append(path+new_path)
            paths = temp
        prev = c
    return paths

input = [
    "480A",
    "143A",
    "983A",
    "382A",
    "974A"
]
for i in input:
    new_s = find_shortest_paths(keypad1, i, "A")
    new_new_s = []
    for s in new_s:
        new_new_s += find_shortest_paths(keypad2, s, "A")
    lol = []
    min = float("inf")
    for s in new_new_s:
        paths = find_shortest_paths(keypad2, s, "A")
        if len(paths[0]) < min:
            min = len(paths[0])
            lol = []
            lol += paths
        elif len(paths[0]) == min:
            lol += paths
    print(i)
    print(min)