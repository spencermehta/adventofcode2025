import sys
from collections import namedtuple

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
lines = [line.split(": ") for line in lines]

E = dict()
for line in lines:
    lhs = line[0]
    E[lhs] = set()
    for rhs in line[1].split():
        E[lhs].add(rhs)



def dfs(node, visited):
    nv = {v for v in visited}
    nv.add(node)
    if node == "out":
        return 1
    ans = 0
    for neighbour in E[node]:
        if neighbour not in nv:
            ans += dfs(neighbour, nv)

    return ans

def dfs2(node, visited):
    nv = {v for v in visited}
    nv.add(node)
    key = (node, "dac" in nv, "fft" in nv)
    if key in M:
        return M[key]
    if node == "out":
        if "dac" in nv and "fft" in nv:
            M[key] = 1
            return 1
        else:
            M[key] = 0 
            return 0
    ans = 0
    for neighbour in E[node]:
        if neighbour not in nv:
            ans += dfs2(neighbour, nv)

    M[key] = ans
    return ans


def part_one():
    return(dfs("you", set()))

def part_two():
    return(dfs2("svr", set()))

M = dict()
print(part_one())
M = dict()
print(part_two())

