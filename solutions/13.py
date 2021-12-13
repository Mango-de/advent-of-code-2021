with open('inputs/13') as f:
    # l = [int(x) for x in f]
    l = f.read().split('\n\n')
    dots = [[int(y) for y in x.split(',')] for x in l[0].splitlines()]
    fold_instructions = [x[11:].split('=') for x in l[1].splitlines()]

# Part 1

board = {}

for x, y in dots:
    board[(y, x)] = '#'

def fold_board(along: str, i: str):
    i = int(i)
    global board
    max_y = max([x[0] for x in board]) + 1
    max_x = max([x[1] for x in board]) + 1
    l = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for k, v in board.items():
        y, x = k
        l[y][x] = v
    j = 0
    if along == 'y':
        upper = []
        lower = []
        for cl, line in enumerate(l):
            new_line_upper = []
            new_line_lower = []
            for c in range(len(line)):
                if cl < i:
                    new_line_upper.append(l[cl][c])
                if cl > i:
                    new_line_lower.append(l[cl][c])
            if new_line_upper:
                upper.append(new_line_upper)
            if new_line_lower:
                lower.append(new_line_lower)
        for cl, line in enumerate(reversed(lower)):
            for c, dot in enumerate(line):
                if dot == '#':
                    upper[cl][c] = dot
        board = {}
        for cl, line in enumerate(upper):
            for c, dot in enumerate(line):
                if dot == '#':
                    j += 1
                board[(cl, c)] = dot
    elif along == 'x':
        left = []
        right = []
        for cl, line in enumerate(l):
            new_line_left = []
            new_line_right = []
            for c in range(len(line)):
                if c < i:
                    new_line_left.append(l[cl][c])
                if c > i:
                    new_line_right.append(l[cl][c])
            left.append(new_line_left)
            right.append(new_line_right)
        for cl, line in enumerate(right):
            for c, dot in enumerate(reversed(line)):
                if dot == '#':
                    left[cl][c] = dot
        board = {}
        for cl, line in enumerate(left):
            for c, dot in enumerate(line):
                if dot == '#':
                    j += 1
                board[(cl, c)] = dot
    return j
    
i = fold_board(*fold_instructions[0])

print(i)

# Part 2

for ins in fold_instructions:
    fold_board(*ins)
    
max_y = max([x[0] for x in board]) + 1
max_x = max([x[1] for x in board]) + 1

r = [[None] * max_x for _ in range(max_y)]

for k, v in board.items():
    y, x = k
    r[y][x] = v
    
print('\n'.join([''.join(x) for x in r]))