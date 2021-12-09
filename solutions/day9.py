from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from helper.submit import *
from utils import *
import networkx as nx


DAY = 9
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def get_neighbours(grid, i, j):
    neighbours = []
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if x == i and y == j:
            continue
        if x < 0 or y < 0:
            continue
        if x >= len(grid) or y >= len(grid[x]):
            continue
        neighbours.append(grid[x][y])
    return neighbours


def part1(lines: List[str]) -> int:
    grid = []
    su = 0
    for line in lines:
        grid.append(list(map(int, list(line))))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if all([grid[i][j] < x for x in get_neighbours(grid, i, j)]):
                su += grid[i][j] + 1
    return su


submit(1, part1(lines), force=False)


# Part 2
##################################################
def get_neighbours(grid, i, j):
    neighbours = []
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if x == i and y == j:
            continue
        if x < 0 or y < 0:
            continue
        if x >= len(grid) or y >= len(grid[x]):
            continue
        neighbours.append(grid[x][y])
    return neighbours


def dfs(i, j, visited, prev=None, grid=None):
    visited.add((i, j))
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if x < 0 or y < 0:
            continue
        if x >= len(grid) or y >= len(grid[x]):
            continue
        if (x, y) in visited:
            continue
        if grid[x][y] > grid[i][j]:
            dfs(x, y, visited, (i, j))


def part2(lines: List[str]) -> int:
    HEIGHT = len(lines)
    WIDTH = len(lines[0])

    grid = {}
    for y, ln in enumerate(lines):
        for x, c in enumerate(ln):
            grid[x, y] = int(c)

    g = nx.Graph()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[x, y] == 9:
                continue

            for dx in [-1, 1]:
                dy = 0
                if grid.get((x + dx, y + dy), 9) != 9:
                    g.add_edge((x, y), (x + dx, y + dy))

            for dy in [-1, 1]:
                dx = 0
                if grid.get((x + dx, y + dy), 9) != 9:
                    g.add_edge((x, y), (x + dx, y + dy))

    sizes = []
    for basin in nx.connected_components(g):
        sizes.append(len(set(basin)))

    x = sorted(sizes)

    return x[-3] * x[-2] * x[-1]


submit(2, part2(lines), force=False)
