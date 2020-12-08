import unittest

from aoc_2020.day_7.problem import *


class TestDay7(unittest.TestCase):

    def test_create_bag_rules(self):
        s = "vibrant plum bags contain 5 faded blue bags.\nfaded blue bags contain no other bags."
        b = BagRule.create_bag_rules(s)
        self.assertEqual("BagColor(color=faded blue)", b["faded blue"].get_tree())
        self.assertEqual("BagColor(color=vibrant plum, rules={BagColor(color=faded blue): 5})", b["vibrant plum"].get_tree())
        self.assertEqual([], b["vibrant plum"].get_parents())
        self.assertEqual("[BagColor(color=vibrant plum, rules={BagColor(color=faded blue): 5})]", str(b["faded blue"].get_parents()))

    def test_example_1(self):
        s = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
        self.assertEqual(4, find_all_parents(s, "shiny gold"))

    def test_part_1(self):
        with open("input.text") as f:
            self.assertEqual(259, find_all_parents(f.read(), "shiny gold"))

    def test_example_2(self):
        s = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
        self.assertEqual(32, count_child_bags(s, "shiny gold"))

    def test_example_3(self):
        s = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
        self.assertEqual(126, count_child_bags(s, "shiny gold"))

    def test_example_3_1(self):
        s = """dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
        self.assertEqual(2, count_child_bags(s, "dark blue"))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(45018, count_child_bags(f.read(), "shiny gold"))


if __name__ == "__main__":
    unittest.main()
