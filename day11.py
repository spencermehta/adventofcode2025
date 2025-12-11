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
    key = (node)
    if key in M:
        print("cached")
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
            ans += dfs(neighbour, nv)
    M[key] = ans
    return ans

def dfs2(node, visited):
    nv = {v for v in visited}
    nv.add(node)
    key = (node)
    if node == "out":
        if "dac" in nv and "fft" in nv:
            return (1,0)
        else:
            return (0,1)
    ans = 0
    for neighbour in E[node]:
        if neighbour not in nv:
            ans += dfs2(neighbour, nv)
    M[key] = ans
    return ans

M = dict()

def bfs(node, path):
    print(node, path)
    if node == "out":
        if "dac" in path and "fft" in path:
            return 1
        else:
            return 0
    np = {p for p in path}
    np.add(node)
    ans = 0
    for neighbour in E[node]:
        if neighbour not in np:
            ans += bfs(neighbour, np)
    return ans


def part_one():
    return(dfs("out", set()))

def part_two():
    return(dfs("svr", set()))

#print(part_one())
print(part_two())

