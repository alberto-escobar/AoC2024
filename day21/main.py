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

def shortest_paths_between_pads(keypad, start_position, end_pad):
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
        queue.append(((x, y+1),path+['v'], visited))
        queue.append(((x-1, y),path+['<'], visited))
        queue.append(((x, y-1),path+['^'], visited))
        queue.append(((x+1, y),path+['>'], visited))
       
    return min_paths

def find_shortest_sequences(keypad, string):
    pad_map = {}
    for j in range(len(keypad)):
        for i in range(len(keypad[j])):
            pad = keypad[j][i]
            pad_map[pad] = (i,j)
    paths = None
    prev = "A"
    for c in string:
        current = pad_map[prev]
        if not paths:
            paths = shortest_paths_between_pads(keypad, current, c)
        else:
            new_paths = shortest_paths_between_pads(keypad, current, c)
            temp = []
            for path in paths:
                for new_path in new_paths:
                    temp.append(path+new_path)
            paths = temp
        prev = c
    return paths

def compute_sequence_score(sequence):
    prev = None
    score = 0
    for c in sequence:
        if prev == None:
            prev = c
            continue
        if c == prev:
            score += 1
    return score

def find_shortest_sequence_length_improved(input, robots):
    button_sequences = find_shortest_sequences(keypad, input)    
    for robot in range(robots-1):
        new_button_sequences = []
        min = float("inf")
        for input in button_sequences:
            sequences = find_shortest_sequences(dpad, input)
            if len(sequences[0]) > min:
                continue
            if len(sequences[0]) < min:
                min = len(sequences[0])
                new_button_sequences = sequences
            elif len(sequences[0]) == min:
                new_button_sequences += sequences
        
        button_sequences = new_button_sequences
        
        best_sequences = []
        best_score = -1
        for sequence in button_sequences:
            score = compute_sequence_score(sequence)
            if score > best_score:
                best_sequences = [sequence]
                best_score = score
            elif score == best_score:
                best_sequences.append(sequence)
        sequences = [best_sequences[0]]
        
    return len(sequences[0])

complexity_sum = 0
for s in data:
    length = find_shortest_sequence_length_improved(s, 3)
    numeric_part = int(s[:-1])
    complexity_sum += length * numeric_part

print(f"part 1: {complexity_sum}")

# When I increase the layers of robots from 3 to 4, I proceed to grind to a halt in my computations.
# Seem like this problem as han exponentially increase amount of sequences at each layer, of the
# robots.

# below I will look to improve on my solution to solve part 2.

keypad = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), 
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), 
            None: (3, 0), "0": (3, 1), "A": (3, 2)
        }

dpad = {
            None: (0, 0), "^": (0, 1), "A": (0, 2), 
            "<": (1, 0), "v": (1, 1), ">": (1, 2)
        }
