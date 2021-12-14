from collections import Counter

with open('inputs/14') as f:
    # l = [int(x) for x in f]
    l = f.read().split('\n\n')
    polymer_template = l[0]
    pair_insertions = [x.split(' -> ') for x in l[1].splitlines()]

# Part 1

polymer = list(polymer_template)

def get_insert_rule(letters: str):
    for lt, ti in pair_insertions:
        if lt == letters:
            return ti

for _ in range(10):
    i = 0
    to_reach = len(polymer) + len(polymer) - 1
    while len(polymer) < to_reach:
        ti = get_insert_rule(''.join(polymer[i:i + 2]))
        polymer.insert(i + 1, ti)
        i += 2

c = Counter()

for l in polymer:
    c[l] += 1
    
highest = max(c.values())
lowest = min(c.values())

print(highest - lowest)

# Part 2

polymer = list(polymer_template)

pair_c = Counter()

for i in range(len(polymer) - 1):
    pair_c[polymer[i] + polymer[i + 1]] += 1

c = Counter()

for l in pair_c:
    c[l[0]] += 1
    c[l[1]] += 1

for _ in range(40):
    new_c = Counter()
    for r, res in pair_insertions:
        if pair_c[r] > 0:
            new_c[r] -= pair_c[r]
            new_c[r[0] + res] += pair_c[r]
            new_c[res + r[1]] += pair_c[r]
            c[res] += pair_c[r]
    for r in new_c:
        pair_c[r] += new_c[r]
    
highest = max(c.values())
lowest = min(c.values())

print(highest - lowest + 2)