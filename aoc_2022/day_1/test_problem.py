import unittest

from aoc_2022.day_1.problem import *
from aoc_2022.common import text_to_list

EXAMPLE_TEXT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


class TestDay1(unittest.TestCase):

    def test_group_by_elf(self):
        self.assertEqual(
            [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]],
            group_by_elf(text_to_list(EXAMPLE_TEXT))
        )

    def test_example_1(self):
        elves = group_by_elf(text_to_list(EXAMPLE_TEXT))
        most_calories, swolest_elf = find_elf_with_most_calories(elves)
        self.assertEqual([7000, 8000, 9000], swolest_elf)
        self.assertEqual(24000, most_calories)

    def test_part_1(self):
        with open("input.text") as f:
            elves = group_by_elf(text_to_list(f.read()))
            most_calories, swolest_elf = find_elf_with_most_calories(elves)
            self.assertEqual(74394, most_calories)

    def test_example_2(self):
        elves = group_by_elf(text_to_list(EXAMPLE_TEXT))
        elves = sort_elves(elves)
        self.assertEqual([7000, 8000, 9000], elves[0])
        self.assertEqual(24000, sum(elves[0]))

    def test_example_3(self):
        elves = group_by_elf(text_to_list(EXAMPLE_TEXT))
        elves = sort_elves(elves)
        self.assertEqual(45000, sum_n_elves(elves, 3))

    def test_part_2(self):
        with open("input.text") as f:
            elves = group_by_elf(text_to_list(f.read()))
            elves = sort_elves(elves)
            self.assertEqual(212836, sum_n_elves(elves, 3))


if __name__ == "__main__":
    unittest.main()
