import time

#create data matrix
file = open("day12/data.txt")
data = file.read().split("\n")


for i in range(len(data)):
    data[i] = list(data[i])

rows = len(data)
cols = len(data[0])




marked = set()

def find_crop(i, j, plant, area_set):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return 0
    if data[i][j] != plant:
        return 0
    if (i, j) in marked or (i, j) in area_set:
        return 0
    
    marked.add((i,j))
    area_set.add((i,j))
    n = find_crop(i-1, j, plant, area_set)
    e = find_crop(i, j+1, plant, area_set)
    s = find_crop(i+1, j, plant, area_set)
    w = find_crop(i, j-1, plant, area_set)

plant_crops = {}
for i in range(rows):
    for j in range(cols):
        if (i, j) in marked:
            continue
        plant = data[i][j]
        if plant not in plant_crops:
            plant_crops[plant] = []
        crop_set = set()
        find_crop(i, j, plant, crop_set)
        plant_crops[plant].append(crop_set)

def count_edges(i , j):
    edges = 0
    plant = data[i][j]
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ]
    for direction in directions:
        view = (i + direction[0], j + direction[1])
        if view[0] < 0 or view[0] >= rows or view[1] < 0 or view[1] >= cols:
            edges += 1
        elif plant != data[view[0]][view[1]]:
            edges += 1
        else:
            continue

    return edges

sum = 0
for plant in plant_crops.keys():
    for crop in plant_crops[plant]:
        area = len(crop)
        edges = 0
        for i, j in crop:
            edges += count_edges(i, j)
        sum += area*edges

print(f"Part 1: {sum}")

def count_corners(i, j, crop_set):
    corners = 0
    top_left = (i-1, j-1)
    if top_left[0] < 0 and top_left[1] < 0:
        corners += 1
    elif (i-1, j) in crop_set and (i, j-1) in crop_set and (i-1, j-1) not in crop_set:
        corners += 1
    elif (i-1, j) not in crop_set and (i, j-1) not in crop_set:
        corners += 1
    else:
        corners += 0
    
    top_right = (i-1, j+1)
    if top_right[0] < 0 and top_right[1] >= cols:
        corners += 1
    elif (i-1, j) in crop_set and (i, j+1) in crop_set and (i-1, j+1) not in crop_set:
        corners += 1
    elif (i-1, j) not in crop_set and (i, j+1) not in crop_set:
        corners += 1
    else:
        corners += 0
    
    bottom_left = (i+1, j-1)
    if bottom_left[0] >= rows and bottom_left[1] < 0:
        corners += 1
    elif (i+1, j) in crop_set and (i, j-1) in crop_set and (i+1, j-1) not in crop_set:
        corners += 1
    elif (i+1, j) not in crop_set and (i, j-1) not in crop_set:
        corners += 1
    else:
        corners += 0

    bottom_left = (i+1, j+1)
    if bottom_left[0] >= rows and bottom_left[1] >= cols:
        corners += 1
    elif (i+1, j) in crop_set and (i, j+1) in crop_set and (i+1, j+1) not in crop_set:
        corners += 1
    elif (i+1, j) not in crop_set and (i, j+1) not in crop_set:
        corners += 1
    else:
        corners += 0
    return corners
    



sum = 0
for plant in plant_crops.keys():
    for crop in plant_crops[plant]:
        area = len(crop)
        corners = 0
        for i, j in crop:
            corners += count_corners(i, j, crop)
        sum += area*corners

print(f"Part 2: {sum}")