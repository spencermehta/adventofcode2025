import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
grid = [list(line) for line in lines]

dirs = [
    (-1,-1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]
Y = len(grid)
X = len(grid[0])

def part_one():
    counter = 0
    for y in range(Y):
        for x in range(X):
            c = grid[y][x]
            if c != '@':
                continue

            adjacent = 0
            for (dy, dx) in dirs:
                ny = y + dy
                nx = x + dx
                if (ny < 0) or (ny >= Y) or (nx < 0) or (nx >= X):
                    continue
                
                nc = grid[ny][nx]
                if nc == '@':
                    adjacent += 1
            if adjacent < 4:
                counter += 1
    return counter

def find_removals():
    removals = []
    for y in range(Y):
        for x in range(X):
            c = grid[y][x]
            if c != '@':
                continue

            adjacent = 0
            for (dy, dx) in dirs:
                ny = y + dy
                nx = x + dx
                if (ny < 0) or (ny >= Y) or (nx < 0) or (nx >= X):
                    continue
                
                nc = grid[ny][nx]
                if nc == '@':
                    adjacent += 1
            if adjacent < 4:
                removals.append((y,x))
    return removals

def remove(removals):
    for (y, x) in removals:
        grid[y][x] = '.'


def part_two():
    counter = 0
    while True:
        removals = find_removals()
        if len(removals) == 0:
            break
        counter += len(removals)
        remove(removals)
    return counter


#print(part_one())
print(part_two())
