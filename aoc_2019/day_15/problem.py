import curses
import shutil
import sys
from collections import defaultdict
from enum import Enum
from typing import List

from aoc_2019.common.intcode import IntCode

SCREEN_TTY = sys.stdout.isatty()
SCREEN_SIZE = shutil.get_terminal_size((0, 0))


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def clockwise(self):
        if self == Direction.NORTH:
            return Direction.EAST
        if self == Direction.EAST:
            return Direction.SOUTH
        if self == Direction.SOUTH:
            return Direction.WEST
        if self == Direction.WEST:
            return Direction.NORTH

    def counterclockwise(self):
        if self == Direction.NORTH:
            return Direction.WEST
        if self == Direction.WEST:
            return Direction.SOUTH
        if self == Direction.SOUTH:
            return Direction.EAST
        if self == Direction.EAST:
            return Direction.NORTH


class RoomObject(Enum):
    EMPTY = -1
    WALL = 0
    FLOOR = 1
    OXYGEN_SYSTEM = 2


class Robot:

    intcode = None
    coords = None
    grid = None
    stdscr = None
    pad = None
    oxygen_location = None
    last_move = None

    def __init__(self, starting_coord: List[int]=None, use_curses=False):
        self.coords = [0, 0] if starting_coord is None else list(starting_coord)
        self.grid = defaultdict(lambda: RoomObject.EMPTY)
        self.grid[tuple(self.coords)] = RoomObject.FLOOR
        self.last_direction = Direction.NORTH
        if use_curses:
            if not SCREEN_TTY:
                raise Exception("Screen is not a tty (whatever that means)")
            # if not SCREEN_SIZE[1] >= 40:
            #     raise Exception(
            #         "Screen isn't big enough, needs to be at least 40 characters tall. {}".format(SCREEN_SIZE)
            #     )
            self.stdscr = curses.initscr()

    def run_intcode(self, program: str):
        self.intcode = IntCode(program)
        self.last_move = Direction.NORTH
        try:
            while True:
                direction = self.pick_next_direction()
                if self.move(direction) == RoomObject.OXYGEN_SYSTEM:
                    self.oxygen_location = self.coords
                if self.oxygen_location and self.coords == [0, 0]:
                    break
                self.print_grid()
        except IntcodeHaltedException:
            pass
        self.print_grid()
        return self.grid

    def move(self, direction: Direction):
        self.intcode.add_to_input_buffer(direction.value)
        target_location = self.attempt_move(direction)
        assert self.grid[tuple(target_location)] != RoomObject.WALL
        output = self.intcode.run()
        self.parse_output(target_location, output, direction)
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

    def parse_output(self, target_location: List[int], output: int, direction: Direction):
        self.grid[tuple(target_location)] = RoomObject(output)
        if output != 0:
            self.coords = target_location
            self.last_move = direction

    def pick_next_direction(self):
        direction_to_check = self.last_move
        direction_list = [direction_to_check.clockwise(), direction_to_check.counterclockwise(), direction_to_check]
        for d in direction_list:
            if self.adjacent_obj(d) == RoomObject.EMPTY:
                return d
        for d in direction_list:
            if self.adjacent_obj(d) != RoomObject.WALL:
                return d
        self.last_move = direction_to_check.clockwise()
        return self.last_move

    def adjacent_obj(self, direction):
        x, y = self.coords
        if direction == Direction.NORTH:
            return self.grid[(x, y - 1)]
        if direction == Direction.SOUTH:
            return self.grid[(x, y + 1)]
        if direction == Direction.WEST:
            return self.grid[(x - 1, y)]
        if direction == Direction.EAST:
            return self.grid[(x + 1, y)]

    def print_grid(self):
        grid = self.get_grid()
        if self.stdscr:
            print(dir(self.stdscr))
            self.stdscr.add_str(0, 0, grid)
            self.stdscr.refresh()
        print(grid + "\n\n")

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
