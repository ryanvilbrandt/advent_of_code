from collections import defaultdict
from enum import Enum
from typing import List

from aoc_2019.common.intcode import IntCode


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


class ArcadeGame:

    intcode = None
    grid = None

    def __init__(self, program: str):
        self.intcode = IntCode(program)
        self.grid = defaultdict(Tile)

    def start_game(self):
        try:
            while True:
                x = self.get_next_intcode_output()
                y = self.get_next_intcode_output()
                tile_id = self.get_next_intcode_output()
                self.create_tile(x, y, tile_id)
        except IntcodeHaltedException:
            pass
        return self.grid

    def get_next_intcode_output(self):
        output = self.intcode.run()
        if self.intcode.halted:
            raise IntcodeHaltedException
        return output

    def create_tile(self, x, y, tile_id):
        self.grid[(x, y)] = Tile(tile_id)

    def get_tile_count(self):
        tiles = list(self.grid.values())
        return dict([(tile, tiles.count(tile)) for tile in set(tiles)])


class IntcodeHaltedException(Exception):
    pass
