import numpy as np
#create data matrix
file = open("day13/data.txt")
data = file.read().split("\n")

data_processed = []
i = 0
for row in data:
    row = row.replace("Button A:", "").replace("Button B:", "").replace("Prize:", "").replace("X+", "").replace("Y+", "").replace("X=", "").replace("Y=", "").replace(",", "").split()
    if len(row) == 0:
        continue
    for i in range(2):
        row[i] = int(row[i])
    data_processed.append(row)

machines = []
i = 0
while i < len(data_processed):
    machine = []
    machine.append(data_processed[i])
    i += 1
    machine.append(data_processed[i])
    i += 1
    machine.append(data_processed[i])
    i += 1
    machines.append(machine)

machines = np.array(machines)

tokens = 0
for machine in machines:
    machine = machine.T
    A = machine[:, :-1]
    b = machine[:, -1] 
    solution = np.linalg.solve(A, b)
    solution[0] = round(solution[0], 3)
    solution[1] = round(solution[1], 3)
    if solution[0]%1 == 0 and solution[1]%1 == 0:
        tokens += solution[0]*3 + solution[1]*1

print(f"Part 1: {tokens}")

data_processed = []
i = 0
for row in data:
    row = row.replace("Button A:", "").replace("Button B:", "").replace("Prize:", "").replace("X+", "").replace("Y+", "").replace("X=", "").replace("Y=", "").replace(",", "").split()
    if len(row) == 0:
        continue
    for i in range(2):
        row[i] = int(row[i])
    data_processed.append(row)

machines = []
i = 0
while i < len(data_processed):
    machine = []
    machine.append(data_processed[i])
    i += 1
    machine.append(data_processed[i])
    i += 1
    data_processed[i][0] += 10000000000000
    data_processed[i][1] += 10000000000000
    machine.append(data_processed[i])
    i += 1
    machines.append(machine)

machines = np.array(machines)
tokens = 0
for machine in machines:
    machine = machine.T
    A = machine[:, :-1]
    b = machine[:, -1] 
    solution = np.linalg.solve(A, b)
    solution[0] = round(solution[0], 3)
    solution[1] = round(solution[1], 3)
    if solution[0]%1 == 0 and solution[1]%1 == 0:
        tokens += solution[0]*3 + solution[1]*1

print(f"Part 2: {tokens}")