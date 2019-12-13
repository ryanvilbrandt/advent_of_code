from collections import defaultdict
from enum import Enum

from aoc_2019.common.intcode import IntCode, EmptyInputBufferException


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


FAST_MODE = False


class ArcadeGame:

    intcode = None
    grid = None
    score = None
    tas_list = None

    def __init__(self, program: str):
        self.intcode = IntCode(program)
        self.grid = defaultdict(lambda: Tile.EMPTY)
        self.score = 0
        self.tas_list = []

    def start_game(self, add_quarter=False):
        if add_quarter:
            self.add_quarter()
        while True:
            try:
                self.read_output()
            except EmptyInputBufferException:
                if not FAST_MODE:
                    self.print_screen()
                tas = self.gameshark()
                self.intcode.add_to_input_buffer(tas if tas is not None else self.get_joystick_input())
            except IntcodeHaltedException:
                break

    def read_output(self):
        x = self.get_next_intcode_output()
        y = self.get_next_intcode_output()
        tile_id = self.get_next_intcode_output()
        if x == -1 and y == 0:
            self.set_score(tile_id)
        else:
            self.create_tile(x, y, tile_id)

    def get_next_intcode_output(self):
        output = self.intcode.run()
        if self.intcode.halted:
            raise IntcodeHaltedException
        return output

    def create_tile(self, x, y, tile_id):
        self.grid[(x, y)] = Tile(tile_id)

    def set_score(self, score):
        self.score = score

    def get_tile_count(self):
        tiles = list(self.grid.values())
        return dict([(tile, tiles.count(tile)) for tile in set(tiles)])

    def add_quarter(self):
        self.intcode.tape[0] += 1

    def get_joystick_input(self):
        if self.tas_list:
            return self.tas_list.pop(0)
        s = input("A = Left, D = Right: ")
        if s == "a":
            return -1
        if s == "d":
            return 1
        return 0

    def gameshark(self):
        ball_x_position = self.intcode.tape[388]
        ball_y_position = self.intcode.tape[389]
        ball_x_direction = self.intcode.tape[390]
        paddle_x_position = self.intcode.tape[392]
        # print((ball_x_position, ball_y_position), ball_x_direction, paddle_x_position)
        # Set Paddle position to ball position
        # self.intcode.tape[392] = ball_x_position
        # new_tape = self.intcode.get_tape()
        # self.check_tape_change(old_tape, new_tape)
        # old_tape = new_tape
        move = 0
        if ball_y_position == 17 and ball_x_position == paddle_x_position:
            move = 0
        elif paddle_x_position < (ball_x_position + ball_x_direction):
            move = 1
        elif paddle_x_position > (ball_x_position + ball_x_direction):
            move = -1
        if not FAST_MODE:
            print("I'm moving {}".format(move))
            input()
        return move

    def check_tape_change(self, old_tape, new_tape):
        for i, old in enumerate(old_tape):
            if old != new_tape[i]:
                print("Change at index {}: {} -> {}".format(i, old, new_tape[i]))

    def print_screen(self):
        print("Score: {}".format(self.score))
        print("")
        grid_coords = self.grid.keys()
        x_coords, y_coords = zip(*grid_coords)
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                value = self.grid[(x, y)]
                self.print_tile(value)
            print("")
        print("")

    @staticmethod
    def print_tile(tile: Tile):
        print({
            Tile.EMPTY: " ",
            Tile.WALL: "#",
            Tile.BLOCK: "@",
            Tile.HORIZONTAL_PADDLE: "T",
            Tile.BALL: ".",
        }[tile], end="")



class IntcodeHaltedException(Exception):
    pass
