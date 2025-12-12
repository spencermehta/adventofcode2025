import sys
from collections import namedtuple
from itertools import combinations

sys.setrecursionlimit(10**6)
file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()

Machine = namedtuple("Machine", ["pattern", "buttons", "joltage"])
lines = f.split("\n")
machines = []
for line in lines:
    pattern = line.replace("[", "").split("]")[0]

    buttons = line.split("]")[1].split("{")[0][1:]
    buttons = buttons[:len(buttons)-1].split(" ")
    buttons = [b.replace("(", "").replace(")", "") for b in buttons]
    buttons = [b.split(",") for b in buttons]
    buttons = [[int(bb) for bb in b] for b in buttons]

    joltage = line.replace("}", "").split("{")[1]
    joltage = [int(n) for n in joltage.split(",")]

    machines.append(Machine(pattern, buttons, joltage))

def check_combination(pattern, button_presses):
    count = [0 for _ in pattern]
    for button in button_presses:
        for single_button in button:
            count[single_button] +=1

    for (i,p) in enumerate(pattern):
        if p == "#":
            if count[i] % 2 == 0:
                return False
        else:
            if count[i] % 2 == 1:
                return False
    return True

def combos(buttons, length):
    return list(combinations(buttons, length))

def get_pattern(joltage):
    return ["." if j % 2 == 0 else "#" for j in joltage]

def working(pattern, buttons):
    working = []
    for i in range(len(pattern)+1):
        cs = combos(buttons, i)
        for c in cs:
            check = check_combination(pattern, c)
            if check:
                working.append(c)
    return working

def reduce_joltage(joltage, combo):
    nj = [j for j in joltage]
    for c in combo:
        for b in c:
            nj[b] -= 1
    return nj

M = dict()

def recurse(joltage, buttons):
    key = (tuple(joltage))
    if key in M:
        return M[key]
    if (all(j == 0 for j in joltage)):
        M[key] = 0
        return 0
    if (any(j < 0 for j in joltage)):
        M[key] = None
        return None
    pattern = get_pattern(joltage)
    possible_combos = working(pattern, buttons)
    ans = []
    for combo in possible_combos:
        reduced = reduce_joltage(joltage, combo)
        if all(x%2 ==0 for x in reduced):
            mult = 2
            p = recurse([r/2 for r in reduced], buttons)
        else:
            mult = 1
            p = recurse(reduced, buttons)
        if p is not None:
            ans.append(len(combo) + mult*p)
    if len(ans) > 0:
        M[key] = min(ans)
        return min(ans)
    M[key] = None
    return None

total = 0
for (machinenum, machine) in enumerate(machines):
    M = dict()
    print(machinenum)
    ans = recurse(machine.joltage, machine.buttons)
    if ans is not None:
        total+=ans
    else:
        print("error")


print(total)
