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

    file = open("day8/output.txt", "w")
    file.write(outputString)
    file.close()
    time.sleep(0.1)

#create data matrix
file = open("day8/data.txt")
data = file.read().split("\n")

for i in range(len(data)):
    data[i] = list(data[i])

rows = len(data)
cols = len(data[0])

antenna_map = {}

for r in range(rows):
    for c in range(cols):
        element = data[r][c]
        if element != ".":
            if element not in antenna_map:
                antenna_map[element] = set()
            antenna_map[element].add((r,c))

def get_delta_vector(A, B):
    dr = A[0] - B[0]
    dc = A[1] - B[1]
    return (dr, dc)

antinode_locations = set()

for frequency in antenna_map.keys():
    locations = antenna_map[frequency]
    for location_A in locations:
        for location_B in locations:
            if location_A == location_B:
                continue
            d = get_delta_vector(location_A, location_B)
            antinode_location = (location_A[0] + d[0],location_A[1] + d[1])
            if antinode_location[0] < 0 or antinode_location[0] >= rows:
                continue
            if antinode_location[1] < 0 or antinode_location[1] >= cols:
                continue
            antinode_locations.add(antinode_location)

print(f"Part 1: {len(antinode_locations)}")

antinode_locations = set()

for frequency in antenna_map.keys():
    locations = antenna_map[frequency]
    for location_A in locations:
        for location_B in locations:
            if location_A == location_B:
                continue
            A = (location_A[0], location_A[1])
            B = (location_B[0], location_B[1])
            d = get_delta_vector(A, B)
            antinode_locations.add(location_A)
            antinode_locations.add(location_B)
            while True:
                antinode_location = (A[0] + d[0], A[1] + d[1])
                if antinode_location[0] < 0 or antinode_location[0] >= rows:
                    break
                if antinode_location[1] < 0 or antinode_location[1] >= cols:
                    break
                antinode_locations.add(antinode_location)
                B = (A[0], A[1])
                A = (antinode_location[0], antinode_location[1])

print(f"Part 2: {len(antinode_locations)}")