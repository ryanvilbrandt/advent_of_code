from collections import defaultdict
from enum import Enum
from typing import List

from aoc_2019.common.intcode import IntCode


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def turn_right(self):
        return Direction((self.value + 1) % 4)

    def turn_left(self):
        return Direction((self.value - 1) % 4)


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Robot:

    coords = None
    direction = None
    grid = None
    painted_spots = set()

    def __init__(self, starting_coord: List[int], direction: Direction=Direction.UP):
        self.coords = list(starting_coord)
        self.direction = direction
        self.grid = defaultdict(lambda: Color.BLACK)
        self.painted_spots = set()

    def get_current_color(self) -> Color:
        return self.grid[tuple(self.coords)]

    def paint(self, color_id: int):
        self.painted_spots.add(tuple(self.coords))
        self.grid[tuple(self.coords)] = Color(color_id)

    def turn(self, direction: int):
        """
        0 is left, 1 is right
        :param direction:
        :return:
        """
        if direction == 0:
            self.direction = self.direction.turn_left()
        else:
            self.direction = self.direction.turn_right()

    def move(self):
        if self.direction == Direction.UP:
            self.coords[1] -= 1
        elif self.direction == Direction.DOWN:
            self.coords[1] += 1
        elif self.direction == Direction.RIGHT:
            self.coords[0] += 1
        elif self.direction == Direction.LEFT:
            self.coords[0] -= 1
        else:
            raise Exception("NonEuclideanPlaneError")

    def run_intcode(self, program: str):
        intcode = IntCode(program)
        try:
            while True:
                intcode.add_to_input_buffer(self.get_current_color().value)
                self.paint(self.get_next_intcode_output(intcode))
                self.turn(self.get_next_intcode_output(intcode))
                self.move()
                # self.print_grid(0, 0, 5, 5)
        except IntcodeHaltedException:
            pass
        return intcode

    @staticmethod
    def get_next_intcode_output(intcode: IntCode):
        output = intcode.run()
        if intcode.halted:
            raise IntcodeHaltedException
        return output

    def count_panels_painted(self):
        return len(self.painted_spots)

    def print_grid(self):
        grid_keys = self.grid.keys()
        x_coords = [a[0] for a in grid_keys]
        y_coords = [a[1] for a in grid_keys]
        min_x = min(x_coords) - 2
        max_x = max(x_coords) + 3
        min_y = min(y_coords) - 2
        max_y = max(y_coords) + 3
        for j in range(min_y, max_y):
            for i in range(min_x, max_x):
                coords = [i, j]
                if coords == self.coords:
                    print({
                        Direction.UP: "^",
                        Direction.RIGHT: ">",
                        Direction.LEFT: "<",
                        Direction.DOWN: "v"
                    }[self.direction], end="")
                else:
                    print("." if self.grid[tuple(coords)] == Color.BLACK else "#", end="")
            print("")
        print("")


class IntcodeHaltedException(Exception):
    pass
