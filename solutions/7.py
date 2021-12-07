with open('inputs/7') as f:
    l = [int(x) for x in f.read().split(',')]
    # l = f.read().splitlines()

# Part 1

fuel = {}

for i in range(min(l), max(l)):
    fuel[i] = sum([abs(i - x) for x in l])

print(min(fuel.values()))

# Part 2

fuel = {}

for i in range(min(l), max(l)):
    fuel[i] = sum([abs(i - x) * (abs(i - x) + 1) // 2 for x in l])

print(min(fuel.values()))