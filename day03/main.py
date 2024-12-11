file = open("day3\data.txt", "r")
data = file.read()
file.close()

def performMulOperatation(string):
    data = string[4:-1].split(",")
    return int(data[0]) * int(data[1])

import re

regex = r'mul\(\d+,\d+\)'
matches = re.findall(regex, data)

sum = 0

for match in matches:
    sum += performMulOperatation(match)

print(f"Part 1 answer: {sum}")

regex = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
matches = re.findall(regex, data)

sum=0
enable = True
for match in matches:
    command = match[0:3]
    print(command)
    if command == "do(":
        enable = True
    elif command == "don":
        enable = False
    elif command == "mul":
        if enable:
            sum += performMulOperatation(match)

print(f"Part 2 answer: {sum}")