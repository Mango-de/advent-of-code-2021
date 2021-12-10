from collections import deque

with open('inputs/10') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# Part 1

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

i = 0

for line in l:
    opened = []
    li = list(line)
    while li:
        c = li.pop(0)
        if c in opening:
            opened.append(c)
        else:
            o = opening[closing.index(c)]
            if opened and opened[-1] == o:
                opened.pop()
            else:
                i += illegal_points[c]
                break

print(i)

# Part 2

repair_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

points = []

for line in l:
    opened = []
    li = list(line)
    while li:
        c = li.pop(0)
        if c in opening:
            opened.append(c)
        else:
            o = opening[closing.index(c)]
            if opened and opened[-1] == o:
                opened.pop()
            else:
                break
    if not li:
        i = 0
        while opened:
            c = opened.pop(-1)
            i *= 5
            i += repair_points[c]
        points.append(i)
        
print(sorted(points)[len(points) // 2])