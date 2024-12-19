import unittest

from aoc_2024.common import text_to_grid
from aoc_2024.day_2.problem import *

EXAMPLE_TEXT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


class TestDay2(unittest.TestCase):

    def test_example_1(self):
        grid = text_to_grid(EXAMPLE_TEXT, convert=int)
        self.assertEqual(2, get_safety_score(grid))

    def test_part_1(self):
        grid = text_to_grid(open("input.text").read(), convert=int)
        self.assertEqual(411, get_safety_score(grid))

    def test_example_2(self):
        grid = text_to_grid(EXAMPLE_TEXT, convert=int)
        self.assertEqual(4, get_safety_score_with_dampening(grid))

    def test_safe_with_dampening(self):
        self.assertEqual(2, check_safety([55, 56, 55, 53, 51, 50]))
        self.assertEqual(2, check_safety([55, 56, 55, 53, 51, 50]))

    def test_part_2(self):
        grid = text_to_grid(open("input.text").read(), convert=int)
        self.assertEqual(461, get_safety_score_with_dampening(grid))
