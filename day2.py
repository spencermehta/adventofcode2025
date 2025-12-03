import sys

sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split(",")
lines = [line.split("-") for line in lines]
lines = [[int(x) for x in line] for line in lines]

def part_one():
    g_ls = []
    for line in lines:
        ls = []
        for i in range(line[0], line[1]+1):
            num = str(i)
            first = num[:len(num)//2]
            second = num[len(num)//2:]
            if first == second:
                ls.append(i)
        g_ls = g_ls + ls

    return sum(g_ls)

def part_two():
    g_ls = []
    for line in lines:
        print(line)
        ls = []
        for i in range(line[0], line[1]+1):
            num = str(i)
            #print("num", num)

            for j in range(1, len(num)//2+1):
                patt = num[:j]
                #print("patt", patt)
                start = j
                end = start+j
                bad = False
                while start < len(num):
                    compare = num[start:end]
                    #print("comp", compare)
                    if patt != compare:
                        bad = True
                        break
                    start += j
                    end += j
                if not bad:
                    ls.append(i)
        print(ls)
        g_ls = g_ls + ls
    return sum(set(g_ls))




#print(part_one())
print(part_two())
