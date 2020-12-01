import unittest

from aoc_2020.day_1.problem import *


class TestDay1(unittest.TestCase):

    def test_example1(self):
        num_list = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(514579, find_match(num_list))

    def test_example1_different_order(self):
        num_list = [675, 1456, 1721, 979, 366, 299]
        self.assertEqual(514579, find_match(num_list))

    def test_example1_different_order_again(self):
        num_list = [675, 1456, 979, 366, 299, 1721]
        self.assertEqual(514579, find_match(num_list))

    def test_part_1(self):
        with open("input.text") as f:
            print(find_match(list(map(int, f.read().strip("\n").split("\n")))))

    def test_example2(self):
        num_list = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(241861950, find_three_match(num_list))

    def test_part_2(self):
        with open("input.text") as f:
            print(find_three_match(list(map(int, f.read().strip("\n").split("\n")))))


if __name__ == "__main__":
    unittest.main()
