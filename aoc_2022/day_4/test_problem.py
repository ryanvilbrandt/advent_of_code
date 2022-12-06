import unittest
from pathlib import Path

from problem import *

EXAMPLE_TEXT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


class TestDay1(unittest.TestCase):

    def test_text_to_assignments(self):
        self.assertEqual(((2, 3), (4, 5)), text_to_assignments("2-3,4-5"))

    def test_is_complete_overlap(self):
        self.assertFalse(is_complete_overlap("2-4,6-8"))
        self.assertFalse(is_complete_overlap("2-3,4-5"))
        self.assertFalse(is_complete_overlap("5-7,7-9"))
        self.assertTrue(is_complete_overlap("2-8,3-7"))
        self.assertTrue(is_complete_overlap("6-6,4-6"))
        self.assertFalse(is_complete_overlap("2-6,4-8"))

    def test_count_complete_overlaps(self):
        self.assertEqual(2, count_complete_overlaps(EXAMPLE_TEXT))

    def test_part_1(self):
        text = Path("input.text").read_text()
        self.assertEqual(532, count_complete_overlaps(text))

    def test_count_overlaps(self):
        self.assertFalse(is_partial_overlap("2-4,6-8"))
        self.assertFalse(is_partial_overlap("2-3,4-5"))
        self.assertTrue(is_partial_overlap("5-7,7-9"))
        self.assertTrue(is_partial_overlap("2-8,3-7"))
        self.assertTrue(is_partial_overlap("6-6,4-6"))
        self.assertTrue(is_partial_overlap("2-6,4-8"))

    def test_count_partial_overlaps(self):
        self.assertEqual(4, count_partial_overlaps(EXAMPLE_TEXT))

    def test_part_2(self):
        text = Path("input.text").read_text()
        self.assertEqual(854, count_partial_overlaps(text))


if __name__ == "__main__":
    unittest.main()
