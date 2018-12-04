from collections import defaultdict
import re

day_3_a_example = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""


def preprocess_input(in_str):
    """
    Converts lines of text into 5-tuples
    #1 @ 2,3: 4x5 => (1, 2, 3, 4, 5)
    :param in_str:
    :return:
    """
    return in_str.strip('\n').split('\n')


class Square:

    reg = "#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    id = None
    offset_x = None
    offset_y = None
    width = None
    height = None
    coords = None

    def __init__(self, s):
        """
        :param s: Ex. #1 @ 2,3: 4x5
        """
        if s is None:
            return
        m = re.match(self.reg, s)
        self.id = int(m.group(1))
        self.offset_x = int(m.group(2))
        self.offset_y = int(m.group(3))
        self.width = int(m.group(4))
        self.height = int(m.group(5))
        self.build()

    def build(self):
        """
        Takes a square info and converts it to a list of coordinate pairs for
        each square inch of the square
        :return:
        """
        self.coords = []
        for i in range(self.width):
            for j in range(self.height):
                self.coords.append(tuple([i + self.offset_x, j + self.offset_y]))

    @staticmethod
    def from_coords(id, coords) -> "Square":
        s = Square(None)
        s.id = id
        s.coords = coords
        if coords:
            x_coords, y_coords = zip(*coords)
            s.offset_x = min(x_coords)
            s.offset_y = min(y_coords)
            s.width = max(x_coords) - s.offset_x
            s.height = max(y_coords) - s.offset_y
        return s

    def print(self, w=None, h=None):
        if w is None:
            w = self.offset_x + self.width + 1
        if h is None:
            h = self.offset_y + self.height + 1
        for y in range(h):
            for x in range(w):
                print(self.id if (x, y) in self.coords else '.', end=' ')
            print()

    def get_overlap(self, s: "Square") -> "Square":
        return Square.from_coords('X', set(self.coords).intersection(s.coords))

    def __str__(self):
        return f"Square(id={repr(self.id)}, offset_x={self.offset_x}, offset_y={self.offset_x}, " \
               f"width={self.width}, height={self.height})"

    def __repr__(self):
        return str(self)


class Map:

    coords = defaultdict(lambda: '.')
    width = 0
    height = 0
    overlap_char = 'X'

    def add_square(self, s: Square):
        for coord in s.coords:
            if self.coords[coord] != '.':
                self.coords[coord] = self.overlap_char
            else:
                self.coords[coord] = s.id

    def print(self, w, h):
        """
        :return:
        """
        for y in range(h):
            for x in range(w):
                print(self.coords[(x, y)], end=' ')
            print()

    def count_overlap(self):
        total_overlap = 0
        for k, v in self.coords.items():
            if v == self.overlap_char:
                total_overlap += 1
        return total_overlap


def day_3_a(in_str):
    s = preprocess_input(in_str)
    # Create Squares
    squares = [Square(sig) for sig in s]
    overlap = Map()
    for i, s in enumerate(squares):
        print(i + 1, '/', len(squares))
        overlap.add_square(s)
    return overlap.count_overlap()


assert day_3_a(day_3_a_example) == 4
# with open("day 3.input") as f:
#     print(day_3_a(f.read()))
