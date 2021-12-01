with open('inputs/1') as f:
    l = [int(x) for x in f]

# Part 1

i1 = -1
last1 = 0
for n in l:
    if n > last1:
        i1 += 1
    last1 = n
print(i1)

# Part 2

i2 = -1
last2 = 0
for c in range(len(l)):
    if c <= 1997:
        _sum = l[c] + l[c + 1] + l[c + 2]
        if _sum > last2:
            i2 += 1
        last2 = _sum
print(i2)