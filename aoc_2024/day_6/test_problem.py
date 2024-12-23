import unittest

from aoc_2024.common import text_to_list, text_to_grid
from aoc_2024.day_6.problem import *

EXAMPLE_TEXT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class TestDay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("input.text") as f:
            cls.input_grid = list(text_to_grid(f.read()))

    def test_turn(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        guard = Guard.from_grid(grid)
        self.assertEqual(Direction.NORTH, guard.direction)
        guard.turn()
        self.assertEqual(Direction.EAST, guard.direction)
        guard.turn()
        self.assertEqual(Direction.SOUTH, guard.direction)
        guard.turn()
        self.assertEqual(Direction.WEST, guard.direction)
        guard.turn()
        self.assertEqual(Direction.NORTH, guard.direction)

    def test_move(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        guard = Guard.from_grid(grid)
        self.assertEqual((4, 6), guard.current_position())
        guard.move()
        self.assertEqual((4, 5), guard.current_position())
        guard.turn()
        guard.move()
        guard.move()
        self.assertEqual((6, 5), guard.current_position())
        guard.turn()
        guard.move()
        guard.move()
        self.assertEqual((6, 7), guard.current_position())
        guard.turn()
        guard.move()
        guard.move()
        self.assertEqual((4, 7), guard.current_position())
        guard.turn()
        guard.move()
        guard.move()
        self.assertEqual((4, 5), guard.current_position())

    def test_move_and_turn(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        guard = Guard.from_grid(grid)
        for _ in range(12):
            guard.move_and_turn()
        self.assertEqual((8, 4), guard.current_position())

    def test_example_1(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertEqual(41, patrol(grid))

    def test_part_1(self):
        self.assertEqual(5145, patrol(self.input_grid))

    def test_check_for_loop(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertFalse(check_for_loop(grid, 0, 0))
        self.assertTrue(check_for_loop(grid, 3, 6))
        self.assertTrue(check_for_loop(grid, 6, 7))
        self.assertTrue(check_for_loop(grid, 7, 7))
        self.assertTrue(check_for_loop(grid, 1, 8))
        self.assertTrue(check_for_loop(grid, 3, 8))
        self.assertTrue(check_for_loop(grid, 7, 9))

    def test_example_2(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertEqual(6, count_loops(grid))

    def test_part_2(self):
        self.assertEqual(1539, count_loops(self.input_grid))
