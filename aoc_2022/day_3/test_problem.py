import unittest
from pathlib import Path

from problem import *

EXAMPLE_TEXT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


class TestDay1(unittest.TestCase):

    def test_find_common_item(self):
        self.assertEqual("p", find_common_item("vJrwpWtwJgWrhcsFMMfFFhFp"))

    def test_find_common_items(self):
        self.assertEqual(["p", "L", "P", "v", "t", "s"], find_common_items(EXAMPLE_TEXT))

    def test_get_priority(self):
        self.assertEqual(16, get_priority("p"))
        self.assertEqual(38, get_priority("L"))
        self.assertEqual(42, get_priority("P"))
        self.assertEqual(22, get_priority("v"))
        self.assertEqual(20, get_priority("t"))
        self.assertEqual(19, get_priority("s"))

    def test_example_1(self):
        items = find_common_items(EXAMPLE_TEXT)
        self.assertEqual(157, get_total_priority(items))

    def test_part_1(self):
        text = Path("input.text").read_text()
        items = find_common_items(text)
        self.assertEqual(7446, get_total_priority(items))

    def test_find_badge(self):
        rucksacks = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
        self.assertEqual("r", find_badge(rucksacks))
        rucksacks = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        self.assertEqual("Z", find_badge(rucksacks))

    def test_find_badges(self):
        self.assertEqual(['r', 'Z'], find_badges(EXAMPLE_TEXT))

    def test_example_2(self):
        items = find_badges(EXAMPLE_TEXT)
        self.assertEqual(70, get_total_priority(items))

    def test_part_2(self):
        text = Path("input.text").read_text()
        items = find_badges(text)
        self.assertEqual(2646, get_total_priority(items))


if __name__ == "__main__":
    unittest.main()
