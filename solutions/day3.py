from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit import *
from utils import *


DAY = 3
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    game_rate = ""
    epsilon = ""
    for x in zip(*lines):
        c = Counter(x)
        game_rate += c.most_common(1)[0][0]
        epsilon += c.most_common()[-1][0]
    return int(game_rate, 2) * int(epsilon, 2)


submit(1, part1(lines))


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    save_lines = lines
    position = 0
    while len(lines) > 1 and position < len(lines[0]):
        linesT = list(zip(*lines))
        c = Counter(linesT[position])
        if c["1"] >= c["0"]:
            most_common = "1"
        else:
            most_common = "0"
        lines = [x for x in lines if x[position] == most_common]
        position += 1
    oxygen_gen = int(lines[0], 2)

    position = 0
    lines = save_lines[:]
    while len(lines) > 1 and position < len(lines[0]):
        linesT = list(zip(*lines))
        c = Counter(linesT[position])
        if c["1"] >= c["0"]:
            least_common = "0"
        else:
            least_common = "1"
        lines = [x for x in lines if x[position] == least_common]
        position += 1
    co2 = int(lines[0], 2)

    return co2 * oxygen_gen


submit(2, part2(lines))
