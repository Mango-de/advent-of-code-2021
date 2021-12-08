with open('inputs/8') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# # Part 1

i = 0

for v in [x.split(' | ')[1] for x in l]:
    for d in v.split(' '):
        if len(d) in (2, 3, 4, 7):
            i += 1

print(i)

# Part 2

def digits_contains(digits, v, i):
    if i not in digits:
        return False
    for c in digits[i]:
        if c not in v:
            return False
    return True

def v_contains(digits, v, i):
    if i not in digits:
        return False
    for c in v:
        if c not in digits[i]:
            return False
    return True

def decode(digits, v):
    for i in digits:
        if len(v) == len(digits[i]) and sorted(v) == sorted(digits[i]):
            return str(i)

i = 0

for line in [x.split(' | ') for x in l]:
    output_values = line[1].split()
    digits = {}
    for v in output_values:
        if len(v) == 2:
            digits[1] = v
        elif len(v) == 3:
            digits[7] = v
        elif len(v) == 4:
            digits[4] = v
        elif len(v) == 7:
            digits[8] = v
    p = -1
    while len(digits) != p:
        p = len(digits)
        input_values = line[0].split()
        for v in input_values:
            if len(v) == 2:
                digits[1] = v
            if len(v) == 3:
                digits[7] = v
            if len(v) == 4:
                digits[4] = v
            if len(v) == 5:
                if digits_contains(digits, v, 1) or digits_contains(digits, v, 7):
                    digits[3] = v
                if v_contains(digits, v, 6):
                    digits[5] = v
                if (3 in digits and not digits_contains(digits, v, 3)) and (5 in digits and not digits_contains(digits, v, 5)):
                    digits[2] = v
            if len(v) == 6:
                if digits_contains(digits, v, 4):
                    digits[9] = v
                if (digits_contains(digits, v, 1) or digits_contains(digits, v, 7)) and (not digits_contains(digits, v, 4)):
                    digits[0] = v
                if (not digits_contains(digits, v, 7)) and (not digits_contains(digits, v, 1)):
                    digits[6] = v
            if len(v) == 7:
                digits[8] = v
    i += int(''.join([decode(digits, x) for x in output_values]))

print(i)