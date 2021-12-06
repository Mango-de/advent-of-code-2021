from functools import lru_cache, cache

with open('inputs/6') as f:
    l = [int(x) for x in f.read().split(',')]
    # l = f.read().splitlines()

# Part 1

def fish_after_days(days: int):
    _days = [0] * 9
    for f in l:
        _days[f] += 1
    for d in range(days):
        c = _days.pop(0)
        _days[6] += c
        _days.append(c)
    return sum(_days)
    
print(fish_after_days(80))

# Part 2

print(fish_after_days(256))