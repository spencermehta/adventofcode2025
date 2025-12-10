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


def part_one():
    total = 0
    for machine in machines:
        m = solve_machine(machine)
        total += m
    return total

print(part_one())
