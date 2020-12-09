import unittest

from aoc_2020.day_9.problem import *


class TestDay9(unittest.TestCase):

    def test_get_all_sums_1(self):
        s = "1\n2\n3\n4"
        self.assertEqual({3, 4, 5, 6, 7}, get_all_sums(map(int, text_to_list(s))))

    def test_get_all_sums_2(self):
        s = "9\n8\n7\n6"
        self.assertEqual({13, 14, 15, 16, 17}, get_all_sums(map(int, text_to_list(s))))

    def test_check_for_invalid_number_1(self):
        s = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n49\n100\n50"
        self.assertEqual(100, load_and_find_invalid_number(s, 25))

    def test_check_for_invalid_number_2(self):
        s = "20\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n21\n22\n23\n24\n25\n45\n26\n64\n65\n66"
        self.assertEqual(65, load_and_find_invalid_number(s, 25))

    def test_example_1(self):
        s = "35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576"
        self.assertEqual(127, load_and_find_invalid_number(s, 5))

    def test_part_1(self):
        with open("input.text") as f:
            self.assertEqual(21806024, load_and_find_invalid_number(f.read(), 25))

    def test_example_2(self):
        s = "35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576"
        self.assertEqual(62, part_2(s, 5))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(2986195, part_2(f.read(), 25))


if __name__ == "__main__":
    unittest.main()
