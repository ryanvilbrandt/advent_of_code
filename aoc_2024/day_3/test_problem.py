import unittest

from aoc_2024.day_3.problem import *

EXAMPLE_TEXT_1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
EXAMPLE_TEXT_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


class TestDay2(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(161, sum_mul_instructions(EXAMPLE_TEXT_1))

    def test_part_1(self):
        self.assertEqual(187833789, sum_mul_instructions(open("input.text").read()))

    def test_example_2(self):
        self.assertEqual(48, sum_mul_instructions_w_do_dont(EXAMPLE_TEXT_2))

    def test_part_2(self):
        self.assertEqual(94455185, sum_mul_instructions_w_do_dont(open("input.text").read()))
