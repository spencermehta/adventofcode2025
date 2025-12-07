import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]

def part_one():
    with open(file_name) as f:
        f = f.read().strip()
    lines = f.split("\n")
    lines = [line.split() for line in lines]
    Y = len(lines)
    X = len(lines[0])
    counter = 0
    for x in range(X):
        op = lines[Y-1][x]
        small_counter = 1 if op == "*" else 0
        for y in range(Y-1):
            if op == "*":
                small_counter *= int(lines[y][x])
            else:
                small_counter += int(lines[y][x])

        counter+=small_counter
    return counter

def part_two():
    with open(file_name) as f:
        f = f.read().strip()
    lines = f.split("\n")
    lines = [list(line) for line in lines]
    Y = len(lines)
    X = len(lines[0])

    counter=0
    nums = ["" for _ in range(X)]
    for y in range(Y):
        line = lines[y]
        for x in range(len(line)):
            c = lines[y][x]
            if c != ' ':
                nums[x] += lines[y][x]

    groups = [[]]
    for el in nums:
        if el == '':
            groups.append([])
            continue
        groups[len(groups)-1].append(el)

    for group in groups:
        op = group[0][len(group[0])-1]
        small_counter = 1 if op == "*" else 0
        for i in range(len(group)):
            if i == 0:
                num = int(group[0][:len(group[0])-1])
            else:
                num = int(group[i])
            if op == "*":
                small_counter *= num
            else:
                small_counter += num

        counter+=small_counter

    return counter
            


print(part_one())
print(part_two())
