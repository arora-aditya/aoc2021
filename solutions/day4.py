from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit.submit import *
from utils import *


DAY = 4
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
class Bingo:
    def __init__(self, lines: List[str]):
        self.bingos = [0 for _ in range(10)]
        self.locations = dict()
        self.su = 0
        for i, line in enumerate(lines):
            for j, num in enumerate(map(int, [x for x in line.split(' ') if x != ""])):
                self.locations[num] = i + j*1j
                self.su += num
    
    def add_number(self, num):
        if num in self.locations:
            coord = self.locations[num]
            i, j = int(coord.real), int(coord.imag)
            self.bingos[i] |= 1 << j
            self.bingos[j + 5] |= 1 << i
            self.su -= num
    
    def is_bingo(self) -> bool:
        return 31 in self.bingos
    
    def sum(self):
        return self.su

def part1(lines: List[str]) -> int:
    bingo_numbers = list(map(int, lines[0].split(',')))
    bingos = []
    bingo_lines = []
    for i, line in enumerate(lines):
        if i < 2:
            continue
        elif line != "":
            bingo_lines.append(line)
            if len(bingo_lines) == 5:
                bingos.append(Bingo(bingo_lines))
                bingo_lines = []

    for num in bingo_numbers:
        for bingo in bingos:
            bingo.add_number(num)
            if bingo.is_bingo():
                return num * bingo.sum()



submit(1, part1(lines))


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    bingo_numbers = list(map(int, lines[0].split(',')))
    bingos = []
    bingo_lines = []
    for i, line in enumerate(lines):
        if i < 2:
            continue
        elif line != "":
            bingo_lines.append(line)
            if len(bingo_lines) == 5:
                bingos.append(Bingo(bingo_lines))
                bingo_lines = []


    bingod = list(range(len(bingos)))
    last_removed = i
    for r, num in enumerate(bingo_numbers):
        for i, bingo in enumerate(bingos):
            if i in bingod:
                bingo.add_number(num)
                if bingo.is_bingo():
                    bingod.remove(i)
                    last_removed = i
        if len(bingod) == 0:
            break
    final_bingo = bingos[last_removed]
    num = bingo_numbers[r]
    return num * final_bingo.sum()

submit(2, part2(lines))


