import unittest

from aoc_2024.common import text_to_grid
from aoc_2024.day_4.problem import *

EXAMPLE_TEXT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

FAIL_TEST = """
.....
.M.S.
..A..
.S.M.
.....
"""


class TestDay2(unittest.TestCase):

    def test_get_string(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertEqual("XMAS", get_string(grid, 5, 0, 1, 0))
        self.assertEqual("XMAS", get_string(grid, 4, 1, -1, 0))
        self.assertEqual("", get_string(grid, 7, 6, 1, 0))

    def test_find_xmas(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertTrue(find_xmas(grid, 6, 4))
        self.assertTrue(find_xmas(grid, 4, 1))
        self.assertFalse(find_xmas(grid, 5, 5))

    def test_example_1(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertEqual(18, find_all_xmas(grid))

    def test_part_1(self):
        grid = list(text_to_grid(open("input.text").read()))
        self.assertEqual(2344, find_all_xmas(grid))

    def test_example_2(self):
        grid = list(text_to_grid(EXAMPLE_TEXT))
        self.assertEqual(9, find_all_x_mas(grid))

    def test_fail(self):
        grid = list(text_to_grid(FAIL_TEST))
        self.assertEqual(0, find_all_x_mas(grid))

    def test_part_2(self):
        grid = list(text_to_grid(open("input.text").read()))
        self.assertEqual(1859, find_all_x_mas(grid))
