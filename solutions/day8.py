from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit import *
from utils import *


DAY = 8
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:

    C = Counter()
    for line in lines:
        words = line.split(" | ")[1].split(" ")
        for word in words:
            C[len(word)] += 1
    return C[2] + C[3] + C[4] + C[7]


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    su = 0
    for line in lines:
        words = line.split(" | ")[0].split(" ")
        mapping = {}
        one_segments = set()
        seven_segments = set()
        four_segments = set()
        six_segments = set()
        fives = []
        for word in sorted(words, key=len):
            se = set(list(word))
            if len(word) == 2:
                mapping["".join(sorted(word))] = 1
                one_segments = se
            elif len(word) == 3:
                mapping["".join(sorted(word))] = 7
                seven_segments = se
            elif len(word) == 4:
                mapping["".join(sorted(word))] = 4
                four_segments = se
            elif len(word) == 5:
                fives.append(se)
            elif len(word) == 6:

                if not one_segments.issubset(se):
                    mapping["".join(sorted(word))] = 6
                    six_segments = se
                elif four_segments.issubset(se):
                    mapping["".join(sorted(word))] = 9
                else:
                    mapping["".join(sorted(word))] = 0
            elif len(word) == 7:
                mapping["".join(sorted(word))] = 8
        assert len(fives) == 3
        five_segments = set()
        three_segments = set()
        for f in fives:
            if len(f - seven_segments) == 2:
                mapping["".join(sorted(f))] = 3
                three_segments = f

            if len(f - six_segments) == 0:
                mapping["".join(sorted(f))] = 5
                five_segments = f
        for f in fives:
            if f != three_segments and f != five_segments:
                mapping["".join(sorted(f))] = 2

        assert len(set(mapping.values())) == 10
        words = line.split(" | ")[1].split(" ")
        i = ""
        for word in words:
            i += str(mapping["".join(sorted(word))])
        su += int(i)

    return su


submit(2, part2(lines), force=False)
