file = open("day22/data.txt")
data = [int(row_string) for row_string in file.read().split("\n")]

def evolve_secret(secret):
    result = ((secret << 6) ^ secret) & 16777215
    result = ((result >> 5) ^ result) & 16777215
    result = ((result << 11) ^ result) & 16777215
    return result

def generate(seed, iterations):
    secret = seed
    for _ in range(iterations):
        secret = evolve_secret(secret)
    return secret

sum = 0
for seed in data:
    sum += generate(seed, 2000)

print(f"part 1: {sum}")

def find_sequence_in_evolution(seed, iterations, cache):
    secret = seed
    sequence = []
    visited = set()
    for _ in range(iterations):
        res = evolve_secret(secret)
        sequence.append((res%10) - (secret%10))
        secret = res
        if len(sequence) == 4:
            key = tuple(sequence)
            if key not in visited:    
                if key not in cache:
                    cache[key] = 0
                cache[key] += res%10
                visited.add(key)
            sequence.pop(0)
                

cache = {}
# data = [1, 2, 3, 2024]
for seed in data:
    find_sequence_in_evolution(seed, 2000, cache)

max = 0
max_key = None
for key, value in cache.items():
    if value > max:
        max = value
        max_key = key

print(f"part 2: {max}")