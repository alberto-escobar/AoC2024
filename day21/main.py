import re

file = open("day21/data.txt")
data = [row_string for row_string in file.read().split("\n")]

keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
]

dpad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

keypad_map = {
            "7": (0, 0), "8": (1, 0), "9": (2, 0), 
            "4": (0, 1), "5": (1, 1), "6": (2, 1),
            "1": (0, 2), "2": (1, 2), "3": (2, 2), 
            None: (0, 3), "0": (1, 3), "A": (2, 3)
         }

dpad_map = {
            None: (0, 0), "^": (1, 0), "A": (2, 0), 
            "<": (0, 1), "v": (1, 1), ">": (2, 1)
        }

def bfs(keypad, start_position, end_pad):
    queue=[(start_position, [], [])]
    min_paths = []
    min_steps = float("inf")
    while queue:
        position, path, visited = queue.pop(0)
        x, y = position 
        if x < 0 or x >= len(keypad[0]) or y < 0 or y >= len(keypad):
            continue
        curr_pad = keypad[y][x]
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
        queue.append(((x, y-1),path+['^'], visited))
        queue.append(((x+1, y),path+['>'], visited))
        queue.append(((x, y+1),path+['v'], visited))
        queue.append(((x-1, y),path+['<'], visited))
       
    return min_paths

shortest_paths = {}

for start in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'A']:
    for row in keypad:
        for pad in row:
            if pad == None:
                continue
            shortest_paths[(start, pad)] = bfs(keypad, keypad_map[start], pad)

for start in ['^', 'A', '<', 'v', '>']:
    for row in dpad:
        for pad in row:
            if pad == None:
                continue
            shortest_paths[(start, pad)] = bfs(dpad, dpad_map[start], pad)

def build_sequence(keys, index, previous_key, current_sequence, result):
    if index == len(keys):
        result.append(current_sequence)
        return
    paths = shortest_paths[(previous_key, keys[index])]
    for path in paths:
        build_sequence(keys, index+1, keys[index], current_sequence + path, result)

def find_shortest_sequence(keys, depth, cache):
    if depth == 0:
        return len(keys)
    if (keys, depth) in cache:
        return cache[(keys, depth)]
    subKeys = re.findall('[<^>v]*A', keys)
    total = 0
    for subKey in subKeys:
        result = []
        build_sequence(subKey, 0, 'A', "", result)
        min = float("inf")
        for seq in result:
            length = find_shortest_sequence(seq, depth-1, cache)
            if length < min:
                min = length
        total += min
    cache[(keys, depth)] = total
    return total

cache = {}
sum = 0
for input in data:
    result = []
    build_sequence(input, 0, "A", "", result)
    min = float('inf')
    for seq in result:
        length = find_shortest_sequence(seq, 2, cache)
        if length < min:
            min = length
    numeric_part = int(input[:-1])
    sum += min*numeric_part

print(f"part 1: {sum}")

cache = {}
sum = 0
for input in data:
    result = []
    build_sequence(input, 0, "A", "", result)
    min = float('inf')
    for seq in result:
        length = find_shortest_sequence(seq, 25, cache)
        if length < min:
            min = length
    numeric_part = int(input[:-1])
    sum += min*numeric_part

print(f"part 2: {sum}")

# this was a very difficult problem.
# kudos to this reddit post, I was 
# very lost and the post helped 
# break it down to me
# https://tinyurl.com/edbzn8w2