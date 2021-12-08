from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from itertools import permutations
from pprint import pprint as pp
from math import *
from helper.submit.submit import *
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
    m = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7,
         "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}

    m = {"".join(sorted(k)):v for k,v in m.items()}

    ans = 0
    for line in lines:
        a,b = line.split(" | ")
        a = a.split(" ")
        b = b.split(" ")
        for perm in permutations("abcdefg"):
            pmap = {a:b for a,b in zip(perm,"abcdefg")}
            anew = ["".join(pmap[c] for c in x) for x in a]
            bnew = ["".join(pmap[c] for c in x) for x in b]
            if all("".join(sorted(an)) in m for an in anew):
                bnew = ["".join(sorted(x)) for x in bnew]
                ans += int("".join(str(m[x]) for x in bnew))
                break
    return ans

submit(2, part2(lines), force=False)


