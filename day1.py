import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")

def part_one():
    i = 50
    counter = 0
    for line in lines:
        d = line[0]
        n = int(line[1:])
        if d == 'L':
            i = (i - n) % 100
        else:
            i = (i + n) % 100
        if i == 0:
            counter+=1
    return counter

def part_two():
    i = 50
    counter = 0
    for line in lines:
        d = line[0]
        n = int(line[1:])
        mult = -1 if d == 'L' else 1
        for _ in range(n):
            i =  (i + mult) % 100
            if i == 0:
                counter+=1
    return counter


print(part_one())
print(part_two())
