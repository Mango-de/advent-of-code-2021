from collections import defaultdict

with open('inputs/11') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# Part 1

board = [[int(y) for y in list(x)] for x in l]

i = 0
octopuses = []

def get_neighbours(x, y):
    result = []
    for xn in range(x - 1, x + 2):
        for yn in range(y - 1, y + 2):
            if (x != xn or y != yn) and xn in range(len(board)) and yn in range(len(board[xn])):
                result.append((xn, yn))
    return result

for _ in range(100):
    flashed = defaultdict(lambda: False)
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] > 9:
                board[x][y] = 0
            octopuses.append((x, y))
    while octopuses:
        x, y = octopuses.pop()
        board[x][y] += 1
        if board[x][y] > 9 and not flashed[(x, y)]:
            i += 1
            flashed[(x, y)] = True
            octopuses.extend(get_neighbours(x, y))
        
print(i)

# Part 2

board = [[int(y) for y in list(x)] for x in l]

i = 0
octopuses = []

while True:
    i += 1
    flashed = defaultdict(lambda: False)
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] > 9:
                board[x][y] = 0
            octopuses.append((x, y))
    while octopuses:
        x, y = octopuses.pop()
        board[x][y] += 1
        if board[x][y] > 9 and not flashed[(x, y)]:
            flashed[(x, y)] = True
            octopuses.extend(get_neighbours(x, y))
    if len(flashed) == len(board) * len(board[0]):
        print(i)
        break