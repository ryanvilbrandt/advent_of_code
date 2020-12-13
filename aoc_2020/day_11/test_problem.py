import unittest

from aoc_2020.day_11.problem import *


EXAMPLE = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


class TestDay11(unittest.TestCase):

    def test_run_cycle(self):
        new_grid = run_cycle_part_1(Grid.from_string(EXAMPLE))
        self.assertEqual(Grid.from_string(EXAMPLE.replace("L", "#")), new_grid)
        new_grid = run_cycle_part_1(new_grid)
        second_round = """
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
"""
        self.assertEqual(Grid.from_string(second_round), new_grid)

    def test_example_1(self):
        stable_grid = """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
"""
        grid = run_until_stable_part_1(Grid.from_string(EXAMPLE))
        self.assertEqual(Grid.from_string(stable_grid), grid)
        self.assertEqual(37, str(grid).count("#"))

    def test_part_1(self):
        with open("input.text") as f:
            grid = run_until_stable_part_1(Grid.from_string(f.read()))
        self.assertEqual(2424, str(grid).count("#"))

    def test_count_seats_1(self):
        grid_str = """
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""
        self.assertEqual(8, count_visible_occupied_seats(Grid.from_string(grid_str), 3, 4))

    def test_count_seats_2(self):
        grid_str = """
.............
.L.L.#.#.#.#.
.............
"""
        self.assertEqual(0, count_visible_occupied_seats(Grid.from_string(grid_str), 1, 1))

    def test_count_seats_3(self):
        grid_str = """
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
"""
        self.assertEqual(0, count_visible_occupied_seats(Grid.from_string(grid_str), 3, 3))

    def test_example_2(self):
        stable_grid = """
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
"""
        grid = run_until_stable_part_2(Grid.from_string(EXAMPLE))
        self.assertEqual(Grid.from_string(stable_grid), grid)
        self.assertEqual(26, str(grid).count("#"))

    def test_part_2(self):
        with open("input.text") as f:
            grid = run_until_stable_part_2(Grid.from_string(f.read()))
        self.assertEqual(2208, str(grid).count("#"))


if __name__ == "__main__":
    unittest.main()
