with open('inputs/6') as f:
    l = [int(x) for x in f.read().split(',')]
    # l = f.read().splitlines()

# Part 1

def fish_after_days(days: int):
    fish = [0] * 9
    for f in l:
        fish[f] += 1
    for _ in range(days):
        c = fish.pop(0)
        fish[6] += c
        fish.append(c)
    return sum(fish)
    
print(fish_after_days(80))

# Part 2

print(fish_after_days(256))
