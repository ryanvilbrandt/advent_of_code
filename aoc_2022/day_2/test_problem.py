import unittest
from pathlib import Path

from problem import *
from aoc_2022.common import text_to_list

EXAMPLE_TEXT = """
A Y
B X
C Z
"""


class TestDay1(unittest.TestCase):

    def test_score_round(self):
        self.assertEqual(4, score_round("A", "X"))
        self.assertEqual(1, score_round("B", "X"))
        self.assertEqual(7, score_round("C", "X"))
        self.assertEqual(8, score_round("A", "Y"))
        self.assertEqual(5, score_round("B", "Y"))
        self.assertEqual(2, score_round("C", "Y"))
        self.assertEqual(3, score_round("A", "Z"))
        self.assertEqual(9, score_round("B", "Z"))
        self.assertEqual(6, score_round("C", "Z"))

    def test_example_1(self):
        self.assertEqual(15, follow_strategy_guide(EXAMPLE_TEXT))

    def test_part_1(self):
        text = Path("input.text").read_text()
        self.assertEqual(11906, follow_strategy_guide(text))

    def test_example_2(self):
        self.assertEqual(12, follow_strategy_guide_v2(EXAMPLE_TEXT))

    def test_part_2(self):
        text = Path("input.text").read_text()
        self.assertEqual(11186, follow_strategy_guide_v2(text))


if __name__ == "__main__":
    unittest.main()
