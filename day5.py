import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
fresh,available = f.split("\n\n")
fresh = fresh.split("\n")
fresh = [l.split('-') for l in fresh]
fresh = [[int(x) for x in pair] for pair in fresh]
available = available.split("\n")
available = [int(n) for n in available]

def part_one():
    sorted_fresh = sorted(fresh, key=lambda x : x[0])
    counter = 0
    for el in available:
        for sel in sorted_fresh:
            if el < sel[0]:
                break
            if el >= sel[0] and el <= sel[1]:
                counter+=1
                break
            if el > sel[1]:
                continue
    return counter

def part_two():
    sorted_fresh = sorted(fresh, key=lambda x : x[0])
    max_seen = 0
    counter = 0
    for sel in sorted_fresh:
        low = max(max_seen+1, sel[0])
        high = sel[1]
        if high >= low:
            diff = high - low +1
            counter += diff
            max_seen = max(max_seen, sel[1])
    return counter





print(part_one())
print(part_two())


