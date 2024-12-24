file = open("day23/data.txt")
data = [row_string.split("-") for row_string in file.read().split("\n")]

map = {}
for connection in data:
    cpu1, cpu2 = connection
    if cpu1 not in map:
        map[cpu1] = set()
    if cpu2 not in map:
        map[cpu2] = set()
    map[cpu1].add(cpu2)
    map[cpu2].add(cpu1)


sets_of_three = set()
for c1 in map.keys(): 
    if c1[0] != "t" or len(map[c1]) < 3:
        continue
    c1_connections = map[c1]
    for c1 in list(c1_connections):
        for c2 in list(c1_connections):
            if c1==c2:
                continue
            if c2 in map[c1] and c1 in map[c2]:
                set_of_three = [c1, c1, c2]
                set_of_three.sort()
                set_of_three = tuple(set_of_three)
                if set_of_three not in sets_of_three:
                    sets_of_three.add(set_of_three)

num = len(sets_of_three)

print(f"part 1: {num}")

# Learned something new today!
# Maximal cliques and bron-kerbosch algorithm.
# credit to:
# https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/

def find_all_cliques(current_clique, candidate, visited, graph):
    if not candidate and not visited:
        yield current_clique
    while candidate:
        v = candidate.pop()
        yield from find_all_cliques(
            current_clique.union({v}),
            candidate.intersection(graph[v]),
            visited.intersection(graph[v]),
            graph
        )
        visited.add(v)

all_cliques = list(find_all_cliques(set(), set(map.keys()), set(), map))

max_clique = set()
for clique in all_cliques:
    if len(clique) > len(max_clique):
        max_clique = clique

max_clique = list(max_clique)
max_clique.sort()
password = ",".join(max_clique)

print(f"part 2: {password}")