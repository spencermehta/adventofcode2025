import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")

def part_one():
    splits = 0
    beams = [set() for _ in lines]
    beams[0].add(lines[0].index('S'))
    for (i, line) in enumerate(lines):
        for beam in beams[i]:
            if i+1 >= len(lines):
                continue
            if lines[i+1][beam] == '^':
                splits += 1
                #if beam-1 >= 0:
                beams[i+1].add(beam-1)
                beams[i+1].add(beam+1)
            else:
                beams[i+1].add(beam)
    return splits

def part_two():
    beam = (lines[0].index('S'), 0)

    return dfs(beam)

M = {}

def dfs(beam):
    if beam in M:
        return M[beam]
    bx, by = beam
    if by == len(lines)-1:
        return 1

    count = 0
    if lines[by+1][bx] == '^':
        count +=dfs((bx-1, by+1))
        count +=dfs((bx+1, by+1))
    else:
        count += dfs((bx, by+1))
    M[beam] = count
    return count

print(part_one())
print(part_two())
