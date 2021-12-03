with open('inputs/3') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# Part 1

_gamma = ''
_epsilon = ''

for i in range(len(l[0])):
    if len([x[i] for x in l if x[i] == '1']) > len([x[i] for x in l if x[i] == '0']): 
        _gamma += '1'
        _epsilon += '0'
    else:
        _gamma += '0'
        _epsilon += '1'

print(int(_gamma, 2) * int(_epsilon, 2))

# Part 2

numbers = l[:]
pos = 0

while len(numbers) > 1:
    bits = []
    for i in numbers:
        bits.append(i[pos])
    if bits.count('1') >= bits.count('0'):
        b = '1'
    else:
        b = '0'
    new = []
    for n in numbers:
        if n[pos] == b:
            new.append(n)
    numbers = new
    pos += 1

oxygen_generator = numbers[0]

numbers2 = l[:]
pos2 = 0

while len(numbers2) > 1:
    bits = []
    for i in numbers2:
        bits.append(i[pos2])
    if bits.count('1') >= bits.count('0'):
        b = '0'
    else:
        b = '1'
    new = []
    for n in numbers2:
        if n[pos2] == b:
            new.append(n)
    numbers2 = new
    pos2 += 1

co2_scrubber = numbers2[0]

print(int(oxygen_generator, 2) * int(co2_scrubber, 2))