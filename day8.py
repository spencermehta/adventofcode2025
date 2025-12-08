import sys
import heapq
from collections import namedtuple

sys.setrecursionlimit(10**6)

Point = namedtuple('Point', ['x','y','z'])

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
lines = [line.split(",") for line in lines]
lines = [[int(n) for n in line] for line in lines]
lines = [Point(line[0], line[1], line[2]) for line in lines]

def dist(p1, p2):
    return abs(((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)**0.5)

def part_one():
    E = set()

    for p1 in lines:
        for p2 in lines:
            if p1 == p2:
                continue
            [pp1, pp2] = sorted([p1, p2])
            E.add((pp1, pp2, dist(p1, p2)))

    E = sorted(E, key=lambda t : t[2])

    C = {p:-1 for p in lines}
    circuits = []
    for p in lines:
        circuits.append(set())
        circuits[len(circuits)-1].add(p)
        C[p] = len(circuits)-1


    i = 0
    max_iters = 1_000
    for e in E:
        (p1, p2, _) = e

        if i == max_iters:
            break
        i+=1

        if C[p1] == C[p2]:
            continue
        else:
            save = C[p2]
            for p in circuits[save]:
                circuits[C[p1]].add(p)
                C[p] = C[p1]
            circuits[save] = set()

    circuit_sizes = sorted([len(c) for c in circuits if len(c) != 0])
    p = 1
    for el in circuit_sizes[-3:]:
        p*= el
    return p

def part_two():
    E = set()

    for p1 in lines:
        for p2 in lines:
            if p1 == p2:
                continue
            [pp1, pp2] = sorted([p1, p2])
            E.add((pp1, pp2, dist(p1, p2)))

    E = sorted(E, key=lambda t : t[2])

    C = {p:-1 for p in lines}
    circuits = []
    for p in lines:
        circuits.append(set())
        circuits[len(circuits)-1].add(p)
        C[p] = len(circuits)-1


    i = 0
    max_iters = 1_000_000
    last_left = None
    last_right = None
    for e in E:
        (p1, p2, _) = e

        if i == max_iters:
            break
        i+=1
        if len(sorted([len(c) for c in circuits if len(c) != 0])) == 1:
            return last_left.x * last_right.x
        
        if C[p1] == C[p2]:
            continue
        else:
            last_left = p1
            last_right = p2
            save = C[p2]
            for p in circuits[save]:
                circuits[C[p1]].add(p)
                C[p] = C[p1]
            circuits[save] = set()

    circuit_sizes = sorted([len(c) for c in circuits if len(c) != 0])
    p = 1
    for el in circuit_sizes[-3:]:
        p*= el
    return p

print(part_one())
print(part_two())

