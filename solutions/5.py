with open('inputs/5') as f:
    # l = [int(x) for x in f]
    l = f.read().splitlines()

# Part 1

class MyDict(dict):
    def __init_subclass__(cls):
        return super().__init_subclass__()
    
    def __getitem__(self, item):
        if (i := self.get(item)) is not None:
            return i
        self[item] = 0
        return self[item]

coordinates = MyDict()

for segment in l:
    left, right = segment.split(' -> ')
    x1, y1 = (int(a) for a in left.split(','))
    x2, y2 = (int(a) for a in right.split(','))
    if x1 == x2:
        coordinates[(x1, y1)] += 1
        while y2 > y1 + 1:
            y1 += 1
            coordinates[(x1, y1)] += 1
        while y2 < y1 - 1:
            y1 -= 1
            coordinates[(x1, y1)] += 1
        coordinates[(x2, y2)] += 1
    elif y1 == y2:
        coordinates[(x1, y1)] += 1
        while x2 > x1 + 1:
            x1 += 1
            coordinates[(x1, y1)] += 1
        while x2 < x1 - 1:
            x1 -= 1
            coordinates[(x1, y1)] += 1
        coordinates[(x2, y2)] += 1
        
print(len([x for x in coordinates.values() if x > 1]))

# Part 2

for segment in l:
    left, right = segment.split(' -> ')
    x1, y1 = (int(a) for a in left.split(','))
    x2, y2 = (int(a) for a in right.split(','))
    if x1 == y1 and x2 == y2:
        coordinates[(x1, y1)] += 1
        while x2 > x1 + 1:
            x1 += 1
            y1 += 1
            coordinates[(x1, y1)] += 1
        while x2 < x1 - 1:
            x1 -= 1
            y1 -= 1
            coordinates[(x1, y1)] += 1
        coordinates[(x2, y2)] += 1
    elif x1 == y2 and x2 == y1:
        coordinates[(x1, y1)] += 1
        while x2 > x1:
            x1 += 1
            y1 -= 1
            coordinates[(x1, y1)] += 1
        while x1 > x2:
            x1 -= 1
            y1 += 1
            coordinates[(x1, y1)] += 1
    elif abs(x2 - x1) == abs(y1 - y2):
        coordinates[(x1, y1)] += 1
        while x2 > x1 and y2 < y1:
            x1 += 1
            y1 -= 1
            coordinates[(x1, y1)] += 1
        while x1 > x2 and y1 < y2:
            x1 -= 1
            y1 += 1
            coordinates[(x1, y1)] += 1
        while x2 > x1 and y2 > y1:
            x1 += 1
            y1 += 1
            coordinates[(x1, y1)] += 1
        while x1 > x2 and y1 > y2:
            x1 -= 1
            y1 -= 1
            coordinates[(x1, y1)] += 1
            
print(len([x for x in coordinates.values() if x > 1]))