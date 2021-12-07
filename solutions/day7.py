from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit.submit import *
from statistics import median
from utils import *


DAY = 7
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    l = list(map(int, lines[0].split(",")))
    k = median(l)
    return int(sum(map(lambda x: abs(x-k), l)))

submit(1, part1(lines), force=True)


# Part 2
##################################################
def su(k):
    return k*(k+1)//2

def part2(lines: List[str]) -> int:
    l = list(map(int, lines[0].split(",")))

    best = float("inf")
    for i in range(min(l), max(l) + 1):
        cost = sum(su(abs(i - j)) for j in l)
        if cost < best:
            best = cost

    return best

submit(2, part2(lines), force=True)


