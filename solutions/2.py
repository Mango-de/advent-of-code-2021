with open('inputs/2') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# Part 1

x = 0
y = 0

for action, steps in [x.split(' ') for x in l]:
    if action == 'forward':
        x += int(steps)
    elif action == 'down':
        y += int(steps)
    elif action == 'up':
        y -= int(steps)

print(x * y)

# Part 2

x = 0
y = 0
aim = 0

for action, steps in [x.split(' ') for x in l]:
    if action == 'forward':
        x += int(steps)
        y += aim * int(steps)
    elif action == 'down':
        aim += int(steps)
    elif action == 'up':
        aim -= int(steps)
        
print(x * y)