from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit.submit import *
from utils import *


DAY = 2
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    coords = 0 + 0j
    for line in lines:
        dir, dist = line.split(" ")
        dist = int(dist)
        if dir.startswith("f"):
            coords += dist 
        elif dir.startswith("d"):
            coords -= dist * 1j
        elif dir.startswith("u"):
            coords += dist * 1j
    
    return int(abs(coords.real) * abs(coords.imag))

submit(1, part1(lines))


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    coords = 0 + 0j
    aim = 0
    for line in lines:
        dir, dist = line.split(" ")
        dist = int(dist)
        if dir.startswith("f"):
            coords += dist 
            coords += aim * dist * 1j
        elif dir.startswith("d"):
            aim += dist
        elif dir.startswith("u"):
            aim -= dist
    
    return int(abs(coords.real) * abs(coords.imag))

submit(2, part2(lines))


