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
        self.assertEqual({1.0: [(1, 1)]}, buckets.left)
        buckets.put_slope_in_bucket((3, 3), (2, 2))
        self.assertEqual({1.0: [(1, 1), (2, 2)]}, buckets.left)
        buckets.put_slope_in_bucket((3, 3), (5, 1))
        self.assertEqual({1.0: [(1, 1), (2, 2)]}, buckets.left)
        self.assertEqual({-1.0: [(5, 1)]}, buckets.right)
        buckets.put_slope_in_bucket((3, 3), (4, 1))
        self.assertEqual({1.0: [(1, 1), (2, 2)]}, buckets.left)
        self.assertEqual({-1.0: [(5, 1)], -2.0: [(4, 1)]}, buckets.right)
        buckets.put_slope_in_bucket((3, 3), (3, 1))
        self.assertEqual({1.0: [(1, 1), (2, 2)]}, buckets.left)
        self.assertEqual({-1.0: [(5, 1)], -2.0: [(4, 1)], -inf: [(3, 1)]}, buckets.right)
        buckets.put_slope_in_bucket((3, 3), (3, 5))
        buckets.put_slope_in_bucket((3, 3), (4, 5))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -inf: [(3, 5)]}, buckets.left)
        self.assertEqual({-1.0: [(5, 1)], -2.0: [(4, 1)], -inf: [(3, 1)], 2.0: [(4, 5)]}, buckets.right)
        buckets.put_slope_in_bucket((3, 3), (0, 3))
        buckets.put_slope_in_bucket((3, 3), (5, 3))
        self.assertEqual({1.0: [(1, 1), (2, 2)], -inf: [(3, 5)], -0.0: [(0, 3)]}, buckets.left)
        self.assertEqual({-1.0: [(5, 1)], -2.0: [(4, 1)], -inf: [(3, 1)], 2.0: [(4, 5)], 0.0: [(5, 3)]}, buckets.right)

    def test_sort_coords(self):
        buckets = SlopeBuckets()
        coords = [(1, 1), (2, 2), (5, 1), (4, 1), (3, 1), (3, 5), (4, 5), (0, 3), (5, 3), (3, 3)]
        buckets.sort_points_into_buckets((3, 3), coords)
        self.assertEqual({1.0: [(1, 1), (2, 2)], -inf: [(3, 5)], -0.0: [(0, 3)]}, buckets.left)
        self.assertEqual({-1.0: [(5, 1)], -2.0: [(4, 1)], -inf: [(3, 1)], 2.0: [(4, 5)], 0.0: [(5, 3)]}, buckets.right)

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

    def test_sort_lists_in_buckets(self):
        buckets = SlopeBuckets()
        origin = (5, 5)
        coords = [
            (2, 2), (4, 4), (3, 3), (1, 1),  # top-left
            (2, 8), (1, 9), (4, 6), (3, 7),  # bottom-left
            (4, 5), (1, 5), (3, 5), (2, 5),  # straight left
            (6, 4), (8, 2), (7, 3), (9, 1),  # top-right
            (9, 9), (8, 8), (7, 7), (6, 6),  # bottom-right
            (9, 5), (6, 5), (7, 5), (8, 5),  # straight right
            (5, 4), (5, 1), (5, 2), (5, 3),  # straight up
            (5, 6), (5, 7), (5, 8), (5, 9)   # straight down
        ]
        buckets.sort_points_into_buckets(origin, coords)
        self.assertEqual(
            {
                -inf: [(5, 6), (5, 7), (5, 8), (5, 9)],
                -1.0: [(2, 8), (1, 9), (4, 6), (3, 7)],
                -0.0: [(4, 5), (1, 5), (3, 5), (2, 5)],
                1.0: [(2, 2), (4, 4), (3, 3), (1, 1)]
            }, buckets.left
        )
        self.assertEqual(
            {
                -inf: [(5, 4), (5, 1), (5, 2), (5, 3)],
                -1.0: [(6, 4), (8, 2), (7, 3), (9, 1)],
                0.0: [(9, 5), (6, 5), (7, 5), (8, 5)],
                1.0: [(9, 9), (8, 8), (7, 7), (6, 6)]
            }, buckets.right
        )

        buckets.sort_lists_in_buckets(origin)
        self.assertEqual(
            {
                -inf: [(5, 6), (5, 7), (5, 8), (5, 9)],
                -1.0: [(4, 6), (3, 7), (2, 8), (1, 9)],
                -0.0: [(4, 5), (3, 5), (2, 5), (1, 5)],
                1.0: [(4, 4), (3, 3), (2, 2), (1, 1)]
            }, buckets.left
        )
        self.assertEqual(
            {
                -inf: [(5, 4), (5, 3), (5, 2), (5, 1)],
                -1.0: [(6, 4), (7, 3), (8, 2), (9, 1)],
                0.0: [(6, 5), (7, 5), (8, 5), (9, 5)],
                1.0: [(6, 6), (7, 7), (8, 8), (9, 9)]
            }, buckets.right
        )

    def test_shoot_all_asteroids_1(self):
        s = """
            .#.
            ###
            .#.
            """
        self.assertEqual([(1, 0), (2, 1), (1, 2), (0, 1)], shoot_all_asteroids(s, (1, 1)))

    def test_shoot_all_asteroids_2(self):
        s = """
            #.#.#
            .###.
            #####
            .###.
            #.#.#
            """
        self.assertEqual([
            (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1),
            (2, 0), (4, 0), (4, 2), (4, 4), (2, 4), (0, 4), (0, 2), (0, 0)
        ], shoot_all_asteroids(s, (2, 2)))

    def test_day_10_example_6(self):
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
        asteroid_list = shoot_all_asteroids(s, (11, 13))
        # Just to make index checking below look better
        asteroid_list = [(inf, inf)] + asteroid_list
        self.assertEqual((11, 12), asteroid_list[1])
        self.assertEqual((12, 1), asteroid_list[2])
        self.assertEqual((12, 2), asteroid_list[3])
        self.assertEqual((12, 8), asteroid_list[10])
        self.assertEqual((16, 0), asteroid_list[20])
        self.assertEqual((16, 9), asteroid_list[50])
        self.assertEqual((10, 16), asteroid_list[100])
        self.assertEqual((9, 6), asteroid_list[199])
        self.assertEqual((8, 2), asteroid_list[200])
        self.assertEqual((10, 9), asteroid_list[201])
        self.assertEqual((11, 1), asteroid_list[299])

    def test_day_10_part_2(self):
        with open("input.text") as f:
            asteroid_list = shoot_all_asteroids(f.read(), (20, 18))
        self.assertEqual((7, 6), asteroid_list[200 - 1])


if __name__ == "__main__":
    unittest.main()
