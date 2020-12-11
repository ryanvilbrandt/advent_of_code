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


def run_cycle(grid: Grid) -> Grid:
    new_grid = grid.copy()
    for x, y, cell in grid:
        if cell != ".":
            adjacent_seats = grid.get_adjacent_cells(x, y)
            if cell == "L" and adjacent_seats.count("#") == 0:
                new_grid.set(x, y, "#")
            elif cell == "#" and adjacent_seats.count("#") >= 4:
                new_grid.set(x, y, "L")
    return new_grid


def run_until_stable(grid: Grid) -> Grid:
    new_grid = run_cycle(grid)
    while new_grid != grid:
        grid = new_grid
        new_grid = run_cycle(grid)
    return new_grid
