from copy import deepcopy
from typing import Tuple, List

from aoc_2020.common import text_to_grid


class Grid:

    def __init__(self, grid: List[List[str]]):
        self.grid = grid

    @staticmethod
    def from_string(text) -> "Grid":
        return Grid(text_to_grid(text))

    def copy(self) -> "Grid":
        return Grid(deepcopy(self.grid))

    def get(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.grid[y][x]
        except IndexError:
            return None

    def set(self, x, y, cell):
        self.grid[y][x] = cell

    def __iter__(self) -> Tuple[int, int, str]:
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                yield x, y, cell

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.grid == other.grid

    def __str__(self):
        return "\n".join(["".join(row) for row in self.grid])

    def __repr__(self):
        return str(self)

    def get_adjacent_cells(self, x, y):
        return [
            self.get(x - 1, y - 1),
            self.get(x - 1, y),
            self.get(x - 1, y + 1),
            self.get(x, y - 1),
            self.get(x, y + 1),
            self.get(x + 1, y - 1),
            self.get(x + 1, y),
            self.get(x + 1, y + 1)
        ]


def count_visible_occupied_seats(grid, x, y):
    directions = [(-1, -1), (-1, +0), (-1, +1),
                  (+0, -1), (+0, +1),
                  (+1, -1), (+1, +0), (+1, +1)]
    visible_occupied_seats = 0
    for d in directions:
        i = 1
        while True:
            seat = grid.get(x + d[0] * i, y + d[1] * i)
            if seat != ".":
                break
            i += 1
        if seat == "#":
            visible_occupied_seats += 1
    return visible_occupied_seats


def run_cycle_part_1(grid: Grid) -> Grid:
    new_grid = grid.copy()
    for x, y, cell in grid:
        if cell != ".":
            seats = grid.get_adjacent_cells(x, y)
            if cell == "L" and seats.count("#") == 0:
                new_grid.set(x, y, "#")
            elif cell == "#" and seats.count("#") >= 4:
                new_grid.set(x, y, "L")
    return new_grid


def run_until_stable_part_1(grid: Grid) -> Grid:
    new_grid = run_cycle_part_1(grid)
    while new_grid != grid:
        grid = new_grid
        new_grid = run_cycle_part_1(grid)
    return new_grid


def run_cycle_part_2(grid: Grid) -> Grid:
    new_grid = grid.copy()
    for x, y, cell in grid:
        if cell != ".":
            visible_occupied_seats = count_visible_occupied_seats(grid, x, y)
            if visible_occupied_seats == 0:
                new_grid.set(x, y, "#")
            elif visible_occupied_seats >= 5:
                new_grid.set(x, y, "L")
    return new_grid


def run_until_stable_part_2(grid: Grid) -> Grid:
    new_grid = run_cycle_part_2(grid)
    while new_grid != grid:
        grid = new_grid
        new_grid = run_cycle_part_2(grid)
    return new_grid
