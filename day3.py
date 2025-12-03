import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
lines = [[int(n) for n in line] for line in lines]

def run_line(line, size):
    line.reverse()
    w = line[:size]
    w.reverse()
    for i in range(size, len(line)):
        saved = line[i]
        for (j, wi) in enumerate(w):
            if saved >= wi:
                w[j] = saved
                saved = wi
            else:
                break
    return w


def part_one():
    counter = 0
    for line in lines:
        arr = run_line(line, 2)
        strarr = [str(n) for n in arr]
        jolt = ''.join(strarr)
        line.reverse()
        counter+=int(jolt)
    print(counter)
def part_two():
    counter = 0
    for line in lines:
        arr = run_line(line, 12)
        strarr = [str(n) for n in arr]
        jolt = ''.join(strarr)
        line.reverse()
        counter+=int(jolt)
    print(counter)

part_one()
part_two()
