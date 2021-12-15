from heapq import heappush, heappop

with open('inputs/15') as f:
    # l = [int(x) for x in f]
    l = [[int(y) for y in x] for x in f.read().splitlines()]

# Part 1

height, width = len(l), len(l[0])

scores = [(0, 0, 0)] # x, y, score
visited = {(0, 0): 0}

def get_neigbours(x, y):
    n = []
    if x > 0:
        n.append([x - 1, y])
    if x < width - 1:
        n.append([x + 1, y])
    if y > 0:
        n.append([x, y - 1])
    if y < height - 1:
        n.append([x, y + 1])
    return n

while True:
    x0, y0, score = heappop(scores)
    if x0 == width - 1 and y0 == height - 1:
        print(score)
        break
    for x, y in get_neigbours(x0, y0):
        new_score = l[y][x] + score
        if not (x, y) in visited or visited[(x, y)] > new_score:
            visited[(x, y)] = new_score
            heappush(scores, (x, y, new_score))