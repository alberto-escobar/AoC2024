import time
#create data matrix
file = open("day14/data.txt")
data = file.read().split("\n")

for i in range(len(data)):
    arr = data[i].replace("p=", "").replace("v=", "").split()
    a = []
    for string in arr:
       string = string.split(",")
       a.append((int(string[0]),int(string[1])))
    data[i] = a

WIDTH = 101
HEIGHT =103

class Robot:
    def __init__(self, position, velocity):
        self.x = position[0]
        self.y = position[1]
        self.dx = velocity[0]
        self.dy = velocity[1]

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x >= WIDTH:
            self.x -= WIDTH
        elif self.x < 0:
            self.x += WIDTH
        if self.y >= HEIGHT:
            self.y -= HEIGHT
        elif self.y < 0:
            self.y += HEIGHT
    
    def getPosition(self):
        return (self.x, self.y)


robots = []
for entry in data:
    robot = Robot(entry[0], entry[1])
    robots.append(robot)


for i in range(100):
    for robot in robots:
        robot.move()

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    x, y = robot.getPosition()
    if x < WIDTH//2 and y < HEIGHT//2:
        q1 += 1
    elif x > WIDTH//2 and y < HEIGHT//2:
        q2 += 1
    elif x < WIDTH//2 and y > HEIGHT//2:
        q3 += 1
    elif x > WIDTH//2 and y > HEIGHT//2:
        q4 += 1
safety_factor = q1*q2*q3*q4
print(f"Part 1: {safety_factor}")

def renderPositions(robots, width, height):
    matrix = []
    for _ in range(height):
        matrix.append(["."]*width)
    
    for robot in robots:
        x, y = robot.getPosition()
        matrix[y][x] = "X"
    
    outputString = ""
    for line in matrix:
        outputString += "".join(line) + "\n"
    file = open("day14/output.txt", "w")
    file.write(outputString)
    file.close()
    time.sleep(0.01)

robots = []
for entry in data:
    robot = Robot(entry[0], entry[1])
    robots.append(robot)

all_unique_positions = -1
for i in range(10000):
    positions = []
    for robot in robots:
        robot.move()
        positions.append(robot.getPosition())
    if len(positions) == len(set(positions)):
        renderPositions(robots, WIDTH, HEIGHT)
        all_unique_positions = i+1

print(f"Part 2: {all_unique_positions}")