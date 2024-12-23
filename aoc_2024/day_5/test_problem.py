import unittest

from aoc_2024.common import text_to_list
from aoc_2024.day_5.problem import *

EXAMPLE_TEXT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


class TestDay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("input.text") as f:
            cls.input_text = f.read()

    def test_example_1(self):
        text_list = text_to_list(EXAMPLE_TEXT)
        self.assertEqual(143, get_middle_page_sum(text_list))

    def test_part_1(self):
        text_list = text_to_list(self.input_text)
        self.assertEqual(5588, get_middle_page_sum(text_list))

    def test_fix_pages(self):
        text_list = text_to_list(EXAMPLE_TEXT)
        rules, _ = get_rules_and_page_lists(text_list)
        self.assertEqual(
            [97, 75, 47, 61, 53],
            fix_pages(rules, [75, 97, 47, 61, 53]),
        )
        self.assertEqual(
            [61, 29, 13],
            fix_pages(rules, [61, 13, 29]),
        )
        self.assertEqual(
            [97, 75, 47, 29, 13],
            fix_pages(rules, [97, 13, 75, 29, 47]),
        )

    def test_example_2(self):
        text_list = text_to_list(EXAMPLE_TEXT)
        self.assertEqual(123, fix_pages_and_get_sum_2(text_list))

    def test_part_2(self):
        text_list = text_to_list(self.input_text)
        self.assertEqual(5331, fix_pages_and_get_sum_2(text_list))
