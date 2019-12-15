from collections import defaultdict
from enum import Enum
from typing import List

from aoc_2019.common.intcode import IntCode


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3


class RoomObject(Enum):
    EMPTY = -1
    WALL = 0
    FLOOR = 1
    OXYGEN_SYSTEM = 2


class Robot:

    intcode = None
    coords = None
    grid = None

    def __init__(self, starting_coord: List[int]=None):
        self.coords = [0, 0] if starting_coord is None else list(starting_coord)
        self.grid = defaultdict(lambda: RoomObject.EMPTY)
        self.grid[tuple(self.coords)] = RoomObject.FLOOR

    def move(self, direction: Direction):
        self.intcode.add_to_input_buffer(direction.value)
        target_location = self.attempt_move(direction)
        output = self.intcode.run()
        self.parse_output(target_location, output)
        return RoomObject(output)

    def attempt_move(self, direction: Direction) -> List[int]:
        attempted_move = self.coords[:]
        if direction == Direction.NORTH:
            attempted_move[1] -= 1
        elif direction == Direction.SOUTH:
            attempted_move[1] += 1
        elif direction == Direction.WEST:
            attempted_move[0] -= 1
        elif direction == Direction.EAST:
            attempted_move[0] += 1
        else:
            raise Exception("NonEuclideanPlaneError")
        return attempted_move

    def parse_output(self, target_location: List[int], output: int):
        self.grid[tuple(target_location)] = RoomObject(output)
        if output != 0:
            self.coords = target_location

    def run_intcode(self, program: str):
        self.intcode = IntCode(program)
        try:
            while True:
                if self.move(Direction.NORTH) == RoomObject.OXYGEN_SYSTEM:
                    break
        except IntcodeHaltedException:
            pass
        return self.intcode

    @staticmethod
    def get_next_intcode_output(intcode: IntCode):
        output = intcode.run()
        if intcode.halted:
            raise IntcodeHaltedException
        return output

    def print_grid(self):
        print(self.get_grid() + "\n\n")

    def get_grid(self) -> str:
        x_coords, y_coords = zip(*self.grid.keys())
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)
        output_lines = []
        for y in range(min_y, max_y + 1):
            output_lines.append("".join([self.get_tile(x, y) for x in range(min_x, max_x + 1)]))
        return "\n".join(output_lines)

    def get_tile(self, x: int, y: int) -> str:
        if [x, y] == self.coords:
            return "D"
        else:
            return {
                RoomObject.EMPTY: " ",
                RoomObject.FLOOR: ".",
                RoomObject.WALL: "#",
                RoomObject.OXYGEN_SYSTEM: "O"
            }[self.grid[(x, y)]]


class IntcodeHaltedException(Exception):
    pass
