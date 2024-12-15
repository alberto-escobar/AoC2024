import time
#create data matrix
file = open("day15/data.txt")
data = file.read().split("\n\n")

warehouse_map = []

for row in data[0].split("\n"):
    warehouse_map.append(list(row))

moves = list(data[1].replace("\n", ""))

moves_map = {
    "^":(0,-1),
    ">":(1,0),
    "v":(0,1),
    "<":(-1,0)
}

walls = set()
boxes = set()
start = None
for y in range(len(warehouse_map)):
    for x in range(len(warehouse_map[y])):
        if warehouse_map[y][x] == "#":
            walls.add((x,y))
        elif warehouse_map[y][x] == "O":
            boxes.add((x,y))
        elif warehouse_map[y][x] == "@":
            start = (x,y)
        else:
            continue

class Robot:
    def __init__(self, pos):
        self.x, self.y = pos
    
    def move(self, dir):
        front_x = self.x + dir[0]
        front_y = self.y + dir[1]
        
        first_box = None
        while (front_x, front_y) in boxes:
            if not first_box:
                first_box = (front_x, front_y)
            front_x += dir[0]
            front_y += dir[1]
        
        if (front_x, front_y) in walls:
            return
        
        self.x += dir[0]
        self.y += dir[1]
        if first_box:
            boxes.remove(first_box)
            boxes.add((front_x, front_y))
        
robot = Robot(start)

for move in moves:
    robot.move(moves_map[move])

sum = 0
for box in list(boxes):
    sum += box[0] + 100*box[1]

print(f"Part 1: {sum}")

warehouse_map = []

for row in data[0].split("\n"):
    new_row = row.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")
    warehouse_map.append(list(new_row))

start = None
for y in range(len(warehouse_map)):
    for x in range(len(warehouse_map[y])):
        if warehouse_map[y][x] == "@":
            start = (x,y)        
        else:
            continue


class NewRobot:
    def __init__(self, pos):
        self.x, self.y = pos
    
    def move(self, dir):
        front_x = self.x + dir[0]
        front_y = self.y + dir[1]

        moving_boxes_stack = []
        if warehouse_map[front_y][front_x] == "#":
            return
        if dir in [(1, 0), (-1, 0)]:
            while warehouse_map[front_y][front_x] in ["[", "]"]:
                moving_boxes_stack.append((front_x, front_y))
                front_x += dir[0]
                front_y += dir[1]
                if warehouse_map[front_y][front_x] == "#":
                    return

        elif dir in [(0, 1), (0, -1)]:
            queue = []
            queue.append((front_x, front_y))
            while len(queue) != 0:
                front_x, front_y = queue.pop(0)
                
                if warehouse_map[front_y][front_x] == "#":
                    return
                
                if warehouse_map[front_y][front_x] == "[":
                    left_side = (front_x, front_y)
                    right_side = (front_x+1, front_y)
                    moving_boxes_stack.append(left_side)
                    moving_boxes_stack.append(right_side)
                    front_left = (left_side[0], left_side[1]+dir[1])
                    front_right = (right_side[0], right_side[1]+dir[1])
                    queue.append(front_left)
                    queue.append(front_right)
                
                elif warehouse_map[front_y][front_x] == "]":
                    right_side = (front_x, front_y)
                    left_side = (front_x-1, front_y)
                    moving_boxes_stack.append(left_side)
                    moving_boxes_stack.append(right_side)
                    front_left = (left_side[0], left_side[1]+dir[1])
                    front_right = (right_side[0], right_side[1]+dir[1])
                    queue.append(front_left)
                    queue.append(front_right)
        
        moving_boxes_stack
        while len(moving_boxes_stack) != 0:
            x, y = moving_boxes_stack.pop()
            if warehouse_map[y][x] == ".":
                continue
            new_x, new_y = (x + dir[0], y + dir[1])
            warehouse_map[new_y][new_x] = warehouse_map[y][x]
            warehouse_map[y][x] = "."

        
        warehouse_map[self.y][self.x] = "."
        self.x += dir[0]
        self.y += dir[1]
        warehouse_map[self.y][self.x] = "@"

robot = NewRobot(start)
def renderToOutput():
    matrix = []
    for j in range(len(warehouse_map)):
        row = []
        for i in range(len(warehouse_map[j])):
            row.append(warehouse_map[j][i])
        matrix.append(row)

    outputString = ""
    for line in matrix:
        outputString += "".join(line) + "\n"

    file = open("day15/output.txt", "w")
    file.write(outputString)
    file.close()
    time.sleep(0.1)



for move in moves:
    robot.move(moves_map[move])
    renderToOutput()

sum = 0
for y in range(len(warehouse_map)):
    for x in range(len(warehouse_map[y])):
        if warehouse_map[y][x] == "[":
            sum += 100*y + x

print(f"Part 2: {sum}")