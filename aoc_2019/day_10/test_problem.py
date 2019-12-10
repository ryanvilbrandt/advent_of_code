import unittest

from aoc_2019.day_10.problem import *


class TestDay7(unittest.TestCase):

    def test_str_to_grid(self):
        s = """
            #.#
            .#.
            """
        self.assertEqual([['#', '.', '#'], ['.', '#', '.']], str_to_grid(s))

    def test_put_slopes_in_buckets(self):
        buckets = SlopeBuckets()
        buckets.put_slope_in_bucket((3, 3), (1, 1))
        self.assertEqual({1.0: [(1, 1)]}, buckets.top)
        buckets.put_slope_in_bucket((3, 3), (2, 2))
        self.assertEqual({1.0: [(1, 1), (2, 2)]}, buckets.top)
        buckets.put_slope_in_bucket((3, 3), (5, 1))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -1.0: [(5, 1)]}, buckets.top)
        buckets.put_slope_in_bucket((3, 3), (4, 1))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -1.0: [(5, 1)], -0.5: [(4, 1)]}, buckets.top)
        buckets.put_slope_in_bucket((3, 3), (3, 1))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -1.0: [(5, 1)], -0.5: [(4, 1)], 0: [(3, 1)]}, buckets.top)
        buckets.put_slope_in_bucket((3, 3), (3, 5))
        buckets.put_slope_in_bucket((3, 3), (4, 5))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -1.0: [(5, 1)], -0.5: [(4, 1)], 0: [(3, 1)]}, buckets.top)
        self.assertEqual({0: [(3, 5)], 0.5: [(4, 5)]}, buckets.bottom)
        buckets.put_slope_in_bucket((3, 3), (0, 3))
        buckets.put_slope_in_bucket((3, 3), (5, 3))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -1.0: [(5, 1)], -0.5: [(4, 1)], 0: [(3, 1)]}, buckets.top)
        self.assertEqual({0: [(3, 5)], 0.5: [(4, 5)]}, buckets.bottom)
        self.assertEqual({"left": [(0, 3)], "right": [(5, 3)]}, buckets.left_or_right)

    def test_sort_coords(self):
        buckets = SlopeBuckets()
        coords = [(1, 1), (2, 2), (5, 1), (4, 1), (3, 1), (3, 5), (4, 5), (0, 3), (5, 3), (3, 3)]
        buckets.sort_points((3, 3), coords)
        self.assertEqual({1.0: [(1, 1), (2, 2)], -1.0: [(5, 1)], -0.5: [(4, 1)], 0: [(3, 1)]}, buckets.top)
        self.assertEqual({0: [(3, 5)], 0.5: [(4, 5)]}, buckets.bottom)
        self.assertEqual({"left": [(0, 3)], "right": [(5, 3)]}, buckets.left_or_right)

    def test_count_visible_asteroids(self):
        coords = [(1, 1), (2, 2), (5, 1), (4, 1), (3, 1), (3, 5), (4, 5), (0, 3), (5, 3), (3, 3)]
        self.assertEqual(8, count_visible_asteroids((3, 3), coords))

    def test_get_all_asteroid_views(self):
        s = """
            #.#.#
            ..#..
            ..#.#
            """
        self.assertEqual({(0, 0): 3, (2, 0): 4, (4, 0): 4, (2, 1): 5, (2, 2): 4, (4, 2): 4}, get_all_asteroid_views(s))

    def test_get_best_view(self):
        s = """
            #.#.#
            ..#..
            ..#.#
            """
        self.assertEqual(((2, 1), 5), get_best_view(s))

    def test_day_10_example_1(self):
        s = """
            .#..#
            .....
            #####
            ....#
            ...##
            """
        self.assertEqual(((3, 4), 8), get_best_view(s))

    def test_day_10_example_2(self):
        s = """
            ......#.#.
            #..#.#....
            ..#######.
            .#.#.###..
            .#..#.....
            ..#....#.#
            #..#....#.
            .##.#..###
            ##...#..#.
            .#....####
            """
        self.assertEqual(((5, 8), 33), get_best_view(s))

    def test_day_10_example_3(self):
        s = """
            #.#...#.#.
            .###....#.
            .#....#...
            ##.#.#.#.#
            ....#.#.#.
            .##..###.#
            ..#...##..
            ..##....##
            ......#...
            .####.###.
            """
        self.assertEqual(((1, 2), 35), get_best_view(s))

    def test_day_10_example_4(self):
        s = """
            .#..#..###
            ####.###.#
            ....###.#.
            ..###.##.#
            ##.##.#.#.
            ....###..#
            ..#.#..#.#
            #..#.#.###
            .##...##.#
            .....#.#..
            """
        self.assertEqual(((6, 3), 41), get_best_view(s))

    def test_day_10_example_5(self):
        s = """
            .#..##.###...#######
            ##.############..##.
            .#.######.########.#
            .###.#######.####.#.
            #####.##.#.##.###.##
            ..#####..#.#########
            ####################
            #.####....###.#.#.##
            ##.#################
            #####.##.###..####..
            ..######..##.#######
            ####.##.####...##..#
            .#####..#.######.###
            ##...#.##########...
            #.##########.#######
            .####.#.###.###.#.##
            ....##.##.###..#####
            .#.#.###########.###
            #.#.#.#####.####.###
            ###.##.####.##.#..##
            """
        self.assertEqual(((11, 13), 210), get_best_view(s))

    def test_day_10_part_1(self):
        with open("input.text") as f:
            self.assertEqual(((20, 18), 280), get_best_view(f.read()))


if __name__ == "__main__":
    unittest.main()
