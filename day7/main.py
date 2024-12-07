import time

#rendering function so I can view how data updates on the file while code runs
#handles converting matrix into printabe string
RENDERING_ON = True
def renderToOutput(data):
    if not RENDERING_ON:
        return
    outputString = ""
    for line in data:
        outputString += "".join(line) + "\n"

    file = open("day6/output.txt", "w")
    file.write(outputString)
    file.close()
    time.sleep(0.01)

#create data matrix
file = open("day7/data.txt")
data = file.read().split("\n")

results = []
terms = []
for i in range(len(data)):
    line = data[i].split(":")
    results.append(int(line[0]))
    line = line[1].split()
    for i in range(len(line)):
        line[i] = int(line[i])
    terms.append(line)

def dfs(numbers, i, current_sum, result):
    if current_sum>result:
        return False
    if i == len(numbers):
        return current_sum == result
    else:
        op1 = current_sum + numbers[i]
        op2 = current_sum * numbers[i]
        return dfs(numbers, i+1, op1, result) or dfs(numbers, i+1, op2, result)

sum = 0
for i in range(len(results)):
    result = results[i]
    if dfs(terms[i], 0, 0, result):
        sum += result
print(f"Part 1: {sum}")

def dfs(numbers, i, current_sum, result):
    if current_sum>result:
        return False
    if i == len(numbers):
        return current_sum == result
    else:
        op1 = current_sum + numbers[i]
        op2 = current_sum * numbers[i]
        op3 = int(str(current_sum) + str(numbers[i]))
        return dfs(numbers, i+1, op1, result) or dfs(numbers, i+1, op2, result) or dfs(numbers, i+1, op3, result)

sum = 0
for i in range(len(results)):
    #print(f"{i+1}/{len(results)}")
    result = results[i]
    if dfs(terms[i], 0, 0, result):
        sum += result
print(f"Part 2: {sum}")