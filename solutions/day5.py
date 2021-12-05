from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit.submit import *
from utils import *


DAY = 5
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    hv_lines = []
    for line in lines:
        c1, c2 = line.split(" -> ")
        x1, y1 = c1.split(",")
        x2, y2 = c2.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        cl = set()
        if x1 == x2:
            my, may = min(y1, y2), max(y1, y2)
            for y in range(my,  may + 1):
                cl.add((x1, y))
        elif y1 == y2:
            mix, mx = min(x1, x2), max(x1, x2)
            for x in range(mix, mx + 1):
                cl.add((x, y1))
        else:
            continue
        hv_lines.append(cl)
    intersecting_coords = set()
    for i, line1 in enumerate(hv_lines):
        for j, line2 in enumerate(hv_lines):
            if i != j:
                intersecting_coords |= (line1 & line2)
    return len(intersecting_coords)
        

# submit(1, part1(lines))


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    hv_lines = []
    for line in lines:
        c1, c2 = line.split(" -> ")
        x1, y1 = c1.split(",")
        x2, y2 = c2.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        cl = set()
        if x1 == x2:
            my, may = min(y1, y2), max(y1, y2)
            for y in range(my,  may + 1):
                cl.add((x1, y))
        elif y1 == y2:
            mix, mx = min(x1, x2), max(x1, x2)
            for x in range(mix, mx + 1):
                cl.add((x, y1))
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            diry = int(copysign(1, y2 - y1)/copysign(1, x2 - x1))

            for i in range(abs(x2 - x1) + 1):
                cl.add((x1 + i, y1 + i*diry))


        hv_lines.append(cl)
    intersecting_coords = set()
    for i, line1 in enumerate(hv_lines):
        for j, line2 in enumerate(hv_lines):
            if i != j:
                intersecting_coords |= (line1 & line2)
    return len(intersecting_coords)

submit(2, part2(lines))


