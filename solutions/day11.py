from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 11
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################




def part1(lines: List[str]) -> int:
    G = []
    for line in lines:
        G.append([int(x) for x in line.strip()])
    R = len(G)
    C = len(G[0])
    ans = 0
    def flash(r,c):
        nonlocal ans
        ans += 1
        G[r][c] = -1
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                rr = r+dr
                cc = c+dc
                if 0 <= rr <R and 0 <= cc <C and G[rr][cc] != -1:
                    G[rr][cc] += 1
                    if G[rr][cc] >= 10:
                        flash(rr,cc)
    t = 0
    while True:
        t += 1
        for r in range(R):
            for c in range(C):
                G[r][c] += 1
        for r in range(R):
            for c in range(C):
                if G[r][c] == 10:
                    flash(r,c)
        for r in range(R):
            for c in range(C):
                if G[r][c] == -1:
                    G[r][c] = 0
        if t == 100:
            return ans
                    
        

submit(1, part1(lines), force=True)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    G = []
    for line in lines:
        G.append([int(x) for x in line.strip()])
    R = len(G)
    C = len(G[0])
    ans = 0
    def flash(r,c):
        nonlocal ans
        ans += 1
        G[r][c] = -1
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                rr = r+dr
                cc = c+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]!=-1:
                    G[rr][cc] += 1
                    if G[rr][cc] >= 10:
                        flash(rr,cc)
    t = 0
    while True:
        t += 1
        for r in range(R):
            for c in range(C):
                G[r][c] += 1
        for r in range(R):
            for c in range(C):
                if G[r][c] == 10:
                    flash(r,c)
        done = True
        for r in range(R):
            for c in range(C):
                if G[r][c] == -1:
                    G[r][c] = 0
                else:
                    done = False
        if done:
            return t

submit(2, part2(lines), force=True)


