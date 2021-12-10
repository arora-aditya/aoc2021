from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit import *
from utils import *
from statistics import median

DAY = 10
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    scoring = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    mapping = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    st = []
    score = 0
    for line in lines:
        for c in line:
            if c in mapping:
                st.append(mapping[c])
                continue
            else:
                if len(st) > 0 and st[-1] != c:
                    score += scoring[c]
                    break
                st.pop()
    return score
                

submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    scoring = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    mapping = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    scores = []
    new_lines = []
    for line in lines:
        st = []
        broken = False
        for c in line:
            if c in mapping:
                st.append(mapping[c])
                continue
            else:
                if len(st) > 0 and st[-1] != c:
                    broken = True
                    break
                st.pop()
        if not broken:
            sc = 0
            for char in reversed(st):
                sc *= 5
                sc += scoring[char]
            scores.append(sc)
    return median(scores)

submit(2, part2(lines), force=False)


