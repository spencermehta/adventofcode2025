import sys
from collections import namedtuple

sys.setrecursionlimit(10**6)
file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = [line.split("\n") for line in f.split("\n\n")]

presents_u = lines[:-1]
presents_u = [present[1:] for present in presents_u]
trees_u = lines[len(lines)-1]

presents = []
for present in presents_u:
    cs = set()
    for y in range(len(present)):
        for x in range(len(present[0])):
            if present[y][x] == "#":
                cs.add((x, y))
    presents.append(cs)

Tree = namedtuple("Tree", ["x", "y", "config"])

trees = []
for t in trees_u:
    size = t.split(":")[0]
    x, y = size.split("x")

    config = t.split(":")[1]
    config = [int(x) for x in config.split()]

    trees.append(Tree(int(x),int(y), config))

def pb(b):
    s = ""
    for y in range(len(b)):
        for x in range(len(b[0])):
            s += b[y][x]
        s += "\n"
    print(s)

def pb2(coords, X, Y):
    s = ""
    for y in range(Y):
        for x in range(X):
            if (x,y) in coords:
                s += "#"
            else:
                s += "."
        s += "\n"
    print(s)


def rotate_coord(x,y, rotation):
    N=3
    if rotation == 0:
        return (x,y)
    elif rotation == 1:
        return (y, N-1-x)
    elif rotation == 2:
        return (N-1-x, N-1-y)
    else:
        return (N-1-y, x)

def rotate(present, rotation):
    return {rotate_coord(x, y, rotation) for (x,y) in present}

"""
###
##.
##.
0,0 1,0 2,0
0,1 1,1    
0,2 1,2    

###
.##
.##
0,0 1,0 2,0
    1,1 2,1
    1,2 2,2
"""
def flip(present, fliption):
    if not fliption:
        return present
    else:
        np = set()
        for (x,y) in present:
            if x == 0:
                np.add((2, y))
            elif x == 1:
                np.add((x, y))
            else :
                np.add((0, y))
        return np

def nxt(x, y, X, Y):
    nx = (x + 1) % X
    ny = y+1 if nx == 0 else y
    return (nx, ny)

def transform(present, rotation, fliption):
    return rotate(flip(present, fliption), rotation)

def can_place(present, board, X, Y):
    for (x,y) in present:
        if x >= X or y >= Y:
            return False
    intersection = present & board
    return len(intersection) == 0

M = dict()

def place(x, y, X, Y, board, remaining_config):
    #pb2(board, X, Y)
    #print(remaining_config)
    key = (x, y, X, Y, tuple(sorted(board)), tuple(remaining_config))
    if key in M:
        return M[key]
    if all(x == 0 for x in remaining_config):
        M[key] = 1
        return 1
    if y >= Y:
        M[key] = 0
        return 0
    """
    dont place
    for each remaining shape
      no flip
        rotate 0
        rotate 1
        rotate 2
        rotate 3
      flip
        rotate 0
        rotate 1
        rotate 2
        rotate 3
    """
    (nx, ny) = nxt(x, y, X, Y)
    placed = 0
    placed += place(nx, ny, X, Y, board, remaining_config)
    if (x,y) not in board:
        for i in range(len(remaining_config)):
            if remaining_config[i] == 0:
                continue
            for fliption in [True, False]:
                for rotation in range(4):
                    transformed_present = transform(presents[i], rotation, fliption)
                    placed_present = {(px + x, py + y) for (px, py) in transformed_present}
                    if can_place(placed_present, board, X, Y):
                        new_board = {c for c in board}
                        for c in placed_present:
                            new_board.add(c)
                        new_rc = []
                        for (j,x) in enumerate(remaining_config):
                            if j != i:
                                new_rc.append(x)
                            else:
                                new_rc.append(x-1)

                        new_placed = place(nx, ny, X, Y, new_board, new_rc)
                        placed += new_placed
                        if placed == 1:
                            return 1
    M[key] = placed
    return placed

def run_tree(tree):
    M = dict()
    cells = tree.x*tree.y
    required_cells = 0
    for (i,c) in enumerate(tree.config):
        required_cells += c*len(presents[i])

    if required_cells>(cells*(3/4)):
        print("too big")
        return 0
    else:
        return 1


    return place(0, 0, tree.x, tree.y, set(), tree.config)


def part_one():
    total = 0
    for (treenum, tree) in enumerate(trees):
        print("tn", treenum)
        if run_tree(tree):
            total += 1
    return total


print(part_one())
