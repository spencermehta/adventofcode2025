import sys
from collections import namedtuple
from itertools import combinations

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

def solve_machine(machine):
    i = 1
    while True:
        cs = combos(machine.buttons, i)
        for c in cs:
            check = check_combination(machine.pattern, c)
            if check:
                return i
        i+=1

def count(current, button):
    nc = [c for c in current]
    for b in button:
        nc[b] +=1
    return nc

def match(joltage, current):
    for (i,j) in enumerate(joltage):
        if j != current[i]:
            return False
    return True

M = dict()

def prune(curr_buttons, joltage):
    ret_buttons = []
    button_tuples = [tuple(b) for b in curr_buttons]
    counters = {button: [0 for _ in joltage] for button in set(button_tuples)}

    for b in curr_buttons:
        counter = counters[tuple(b)]
        avail = True
        for single in b:
            if counter[single] >= joltage[single]:
                avail = False
        if avail:
            for single in b:
                counter[single] +=1
            ret_buttons.append(b)
    return ret_buttons

def prioritize(curr_buttons, joltage):
    #return sorted(curr_buttons, key=lambda b: len(b), reverse=True)
    return sorted(curr_buttons, key=lambda b: sum([joltage[bb] for bb in b]), reverse=True)


M = dict()

def dfs(joltage, max_depth, current, pressed, buttons, depth):
    key = (max_depth, tuple(current), tuple(sorted(pressed)))
    #print(key)
    if key in M:
        return M[key]
    if match(joltage, current):
        M[key] = depth
        return depth
    if depth == max_depth:
        M[key] = None
        return None
    current = count(current, pressed)

    allowed_buttons = prune(buttons, joltage)
    subs = []
    for b in allowed_buttons:
        ans = dfs(joltage, max_depth, current, b, allowed_buttons, depth+1)
        if ans != None:
            M[key] = None
            return ans
            subs.append(ans)
    if len(subs) >= 1:
        M[key] =min(subs)
        return min(subs)
    M[key] = None
    return None


def solve_machine_2(machine):
    i = 1
    while True:
        print("max depth",  i)
        for start_button in machine.buttons:
            prio_buttons = prioritize(machine.buttons, machine.joltage)
            ans = dfs(machine.joltage, i, [0 for _ in machine.joltage], start_button, prio_buttons, 0)
            if ans != None:
                print("success")
                return ans
        i+=1

def part_one():
    total = 0
    for machine in machines:
        m = solve_machine(machine)
        total += m
    return total

def part_two():
    M = dict()
    total = 0
    for machine in machines:
        m = solve_machine_2(machine)
        total += m
    return total

#print(part_one())
print(part_two())
