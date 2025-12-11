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

def check_joltage(joltage, button_presses):
    count = [0 for _ in pattern]
    for button in button_presses:
        for single_button in button:
            count[single_button] +=1
    for (i,j) in enumerate(joltage):
        if j != count[i]:
            return False
    return True

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

def combos(buttons, length):
    return list(combinations(buttons, length))

def solve_machine(machine, curr_buttons, buttons, d):
    if d == 8:
        return -100
    i = 1
    while i <= (len(machine.buttons) * d):
        cs = combos(prune(curr_buttons, machine.joltage), i)
        for c in cs:
            check = check_joltage(machine.joltage, c)
            if check:
                print("success")
                return i
        i+=1
    return solve_machine(machine, curr_buttons + buttons, buttons, d+1)

def solve_machine_up(machine):
	return solve_machine(machine, machine.buttons, machine.buttons, 1)

def part_one():
    total = 0
    for machine in machines:
        m = solve_machine_up(machine)
        print(machine, m)
        total += m
    return total

print(part_one())
