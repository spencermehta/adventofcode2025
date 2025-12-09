import sys
from collections import namedtuple

"""
with pypy3 it runs in reasonable time...
"""

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
lines = [line.split(",") for line in lines]
lines = [[int(n) for n in line] for line in lines]

def part_one():
	max_area = 0
	
	for p1 in lines:
		for p2 in lines:
			if p1 == p2:
				continue
			area = (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)
			if area > max_area:
				max_area = area
	return max_area

Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["l", "r"])

points = [Point(line[0], line[1]) for line in lines]

def is_green(p1, p2, drawn_lines):
    for line in drawn_lines:
        (l1, l2) = line
        if l1.x == l2.x:
            if intersects_vert(p1, p2, line):
                return False
        else:
            if intersects_horiz(p1, p2, line):
                return False
    return True

def intersects_vert(p1, p2, line):
    min_x = min(p1.x, p2.x)
    max_x = max(p1.x, p2.x)
    if line.l.x > min_x and line.l.x < max_x:
        if max(line.l.y, line.r.y) <= min(p1.y, p2.y) or min(line.l.y, line.r.y) >= max(p1.y, p2.y):
            return False

        return True
    return False

def intersects_horiz(p1, p2, line):
    min_y = min(p1.y, p2.y)
    max_y = max(p1.y, p2.y)
    if line.l.y > min_y and line.l.y < max_y:
        if max(line.l.x, line.r.x) <= min(p1.x, p2.x) or min(line.l.x, line.r.x) >= max(p1.x, p2.x):
            return False

        return True
    return False

def part_two():
    max_area = 0
    drawn_lines = []
    for i in range(len(points)):
        p1 = points[i]
        if i == len(points)-1:
            p2 = points[0]
        else:
            p2 = points[i+1]

        drawn_lines.append(Line(p1, p2))

    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue

            if not is_green(p1, p2, drawn_lines):
                continue

            area = (abs(p1.x-p2.x)+1) * (abs(p1.y-p2.y)+1)
            if area > max_area:
                max_area = area

    return max_area

print(part_one())
print(part_two())	
