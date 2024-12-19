file = open("day19/data.txt")
data = file.read().split("\n\n")

available_towels = data[0].split(", ")
desired_displays = data[1].split("\n")

cache = {}

def recurse(design):
    # base case
    if len(design) == 0:
        return 1
    
    # check cache if this has been done before
    if design in cache:
        return cache[design]
    
    # recursion
    sum = 0
    for towel in available_towels:
        if design.startswith(towel):
            sum += recurse(design[len(towel):])
    
    # memoize
    cache[design] = sum
    return sum

count = 0
ways = 0
for display in desired_displays:
    if recurse(display):
        count += 1
        ways += recurse(display)

print(f"part 1: {count}")
print(f"part 2: {ways}")

#   ╱|、
# (˚ˎ 。7  
#  |、˜〵          
# じしˍ,)ノ