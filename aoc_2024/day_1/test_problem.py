import unittest

from aoc_2024.day_1.problem import *

EXAMPLE_TEXT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


class TestDay1(unittest.TestCase):

    def test_example_1(self):
        list_a, list_b = make_lists(EXAMPLE_TEXT)
        self.assertEqual(11, sort_and_compare(list_a, list_b))

    def test_part_1(self):
        list_a, list_b = make_lists(open("input.text").read())
        self.assertEqual(1765812, sort_and_compare(list_a, list_b))

    def test_example_2(self):
        list_a, list_b = make_lists(EXAMPLE_TEXT)
        self.assertEqual(31, similarity_score(list_a, list_b))

    def test_part_2(self):
        list_a, list_b = make_lists(open("input.text").read())
        self.assertEqual(20520794, similarity_score(list_a, list_b))
