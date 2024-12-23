from copy import deepcopy
from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


Grid = list[list[str]]


class Guard:

    def __init__(self, x: int, y: int, direction: Direction, grid: Grid):
        self.x, self.y, self.direction, self.grid = x, y, direction, grid
        self.starting_x, self.starting_y, self.starting_direction = x, y, direction
        grid[y][x] = "."

    @staticmethod
    def from_grid(grid: Grid) -> "Guard":
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell in [".", "#"]:
                    continue
                if cell == "^":
                    direction = Direction.NORTH
                elif cell == ">":
                    direction = Direction.EAST
                elif cell == "v":
                    direction = Direction.SOUTH
                elif cell == "<":
                    direction = Direction.WEST
                else:
                    raise ValueError(cell)
                return Guard(x, y, direction, grid)

    def get_next_space(self) -> tuple[int, int]:
        if self.direction == Direction.NORTH:
            x, y = self.x, self.y - 1
        elif self.direction == Direction.EAST:
            x, y = self.x + 1, self.y
        elif self.direction == Direction.SOUTH:
            x, y = self.x, self.y + 1
        elif self.direction == Direction.WEST:
            x, y = self.x - 1, self.y
        else:
            raise ValueError(self.direction)
        if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid):
            # self.print_grid()
            raise LeftArea(x, y)
        return x, y

    def move(self):
        self.x, self.y = self.get_next_space()

    def turn(self):
        self.direction = Direction((self.direction.value % 4) + 1)

    def current_position(self) -> tuple[int, int]:
        return self.x, self.y

    def move_and_turn(self):
        """
        Moves forward, turning first if needed.
        """
        x, y = self.get_next_space()
        if self.grid[y][x] == "#":
            self.turn()
        self.move()

    def print_grid(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if (x, y) == self.current_position():
                    if self.direction == Direction.NORTH:
                        print("^", end=" ")
                    elif self.direction == Direction.EAST:
                        print(">", end=" ")
                    elif self.direction == Direction.SOUTH:
                        print("v", end=" ")
                    elif self.direction == Direction.WEST:
                        print("<", end=" ")
                else:
                    print(self.grid[y][x], end=" ")
            print("")
        print("")

    def reset_patrol(self):
        self.x, self.y, self.direction = self.starting_x, self.starting_y, self.starting_direction


class LeftArea(Exception):
    pass


def patrol(grid: Grid) -> int:
    guard = Guard.from_grid(grid)
    try:
        while True:
            x, y = guard.current_position()
            grid[y][x] = "X"
            guard.move_and_turn()
    except LeftArea:
        pass
    return sum([row.count("X") for row in grid])


def check_for_loop(grid: Grid, x: int, y: int) -> bool:
    """
    Places obstacle in the given spot, and checks for a loop in the guard's patrol
    """
    grid = deepcopy(grid)
    grid[y][x] = "#"
    guard = Guard.from_grid(grid)
    previous_positions = set()
    try:
        while True:
            # guard.print_grid()
            position = (guard.current_position(), guard.direction)
            if position in previous_positions:
                return True
            previous_positions.add(position)
            guard.move_and_turn()
    except LeftArea:
        return False


def count_loops(grid: Grid):
    loops = 0
    for y, row in enumerate(grid):
        print(f"Checking row {y}")
        for x, cell in enumerate(row):
            if cell == ".":
                if check_for_loop(grid, x, y):
                    loops += 1
    return loops
