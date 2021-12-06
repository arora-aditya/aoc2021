from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit.submit import *
from utils import *


DAY = 6
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    state = Counter(list(map(int, lines[0].split(","))))
    for _ in range(80):
        next_state = Counter()
        for k, ct in state.items():
            if k == 0:
                next_state[6] += ct
                next_state[8] += ct
            else:
                next_state[k - 1] += ct
        state = next_state.copy()
    return sum(next_state.values())
            


submit(1, part1(lines), force=True)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    state = Counter(list(map(int, lines[0].split(","))))
    for _ in range(256):
        next_state = Counter()
        for k, ct in state.items():
            if k == 0:
                next_state[6] += ct
                next_state[8] += ct
            else:
                next_state[k - 1] += ct
        state = next_state.copy()
    return sum(next_state.values())

submit(2, part2(lines), force=True)


