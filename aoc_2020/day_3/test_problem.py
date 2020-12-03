import unittest

from aoc_2020.common import text_to_grid
from aoc_2020.day_3.problem import *


EXAMPLE_GRID = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


class TestDay3(unittest.TestCase):

    def test_check_for_tree_on_grid(self):
        grid = text_to_grid(EXAMPLE_GRID)
        self.assertEqual(False, check_for_tree_on_grid(grid, 3, 1))
        self.assertEqual(True, check_for_tree_on_grid(grid, 6, 2))
        self.assertEqual(False, check_for_tree_on_grid(grid, 9, 3))
        self.assertEqual(True, check_for_tree_on_grid(grid, 12, 4))
        self.assertEqual(True, check_for_tree_on_grid(grid, 15, 5))
        self.assertEqual(False, check_for_tree_on_grid(grid, 18, 6))
        self.assertEqual(True, check_for_tree_on_grid(grid, 21, 7))
        self.assertEqual(True, check_for_tree_on_grid(grid, 24, 8))
        self.assertEqual(True, check_for_tree_on_grid(grid, 27, 9))
        self.assertEqual(True, check_for_tree_on_grid(grid, 30, 10))

    def test_example_1(self):
        grid = text_to_grid(EXAMPLE_GRID)
        self.assertEqual(7, check_path(grid, 3, 1))

    def test_part_1(self):
        with open("input.text") as f:
            grid = text_to_grid(f.read())
        self.assertEqual(220, check_path(grid, 3, 1))

    def test_example_2(self):
        grid = text_to_grid(EXAMPLE_GRID)
        self.assertEqual(336, check_all_paths(grid))

    def test_part_2(self):
        with open("input.text") as f:
            grid = text_to_grid(f.read())
        self.assertEqual(2138320800, check_all_paths(grid))


if __name__ == "__main__":
    unittest.main()
