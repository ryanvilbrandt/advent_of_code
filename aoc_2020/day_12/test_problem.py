import unittest

from aoc_2020.day_12.problem import *


class TestDay12(unittest.TestCase):

    def test_turn(self):
        self.assertEqual(Direction.NORTH, turn(Direction.EAST, -90))
        self.assertEqual(Direction.SOUTH, turn(Direction.EAST, 90))
        self.assertEqual(Direction.NORTH, turn(Direction.WEST, 90))
        self.assertEqual(Direction.WEST, turn(Direction.NORTH, -90))

    def test_move(self):
        self.assertEqual(Coords(5, 0), move(Coords(0, 0), Direction.EAST, 5))

    def test_example_1(self):
        example = """
        F10
        N3
        F7
        R90
        F11
        """
        self.assertEqual(25, run_instructions_part_1(example))

    def test_part_1(self):
        with open("input.text") as f:
            self.assertEqual(1533, run_instructions_part_1(f.read()))

    def test_example_2(self):
        example = """
        F10
        N3
        F7
        R90
        F11
        """
        self.assertEqual(286, run_instructions_part_2(example))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(25235, run_instructions_part_2(f.read()))


if __name__ == "__main__":
    unittest.main()
