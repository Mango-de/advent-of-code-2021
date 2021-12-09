from collections import deque
from functools import reduce
from operator import mul

with open('inputs/9') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# Part 1

board = [[int(y) for y in list(x)] for x in l]

low_point_risk_levels = []

for x in range(len(board)):
    for y in range(len(board[x])):
        checks = []
        n = board[x][y]
        if x >= 1:
            checks.append(board[x - 1][y] > n)
        if x <= len(board) - 2:
            checks.append(board[x + 1][y] > n)
        if y >= 1:
            checks.append(board[x][y - 1] > n)
        if y <= len(board[x]) - 2:
            checks.append(board[x][y + 1] > n)
        if all(checks):
            low_point_risk_levels.append(n + 1)

print(sum(low_point_risk_levels))

# Part 2

board = {}
for ridx, row in enumerate(l):
    for cidx, column in enumerate(row):
        board[cidx+1j*ridx] = int(column)

basins = []
processed = set()
q = deque()

for pos, n in board.items():
    if pos in processed or n == 9:
        continue
    basin = set()
    q.append(pos)
    while len(q) > 0:
        pos = q.popleft()
        if pos in processed:
            continue
        height = board.get(pos, 9)
        if height == 9:
            continue
        basin.add(pos)
        processed.add(pos)
        q.extend(pos + d for d in (1, -1, 1j, -1j))
    basins.append(len(basin))

print(reduce(mul, sorted(list(basins))[-3:]))