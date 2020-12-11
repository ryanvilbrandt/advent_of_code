import unittest

from aoc_2020.day_10.problem import *


class TestDay10(unittest.TestCase):

    def test_example_1(self):
        s = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4"
        self.assertEqual(35, part_1(s))

    def test_example_2(self):
        s = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3"
        self.assertEqual(220, part_1(s))

    def test_part_1(self):
        with open("input.text") as f:
            self.assertEqual(2170, part_1(f.read()))

    def test_example_3_brute_force(self):
        s = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4"
        self.assertEqual(8, part_2_brute_force(s))

    def test_example_4_brute_force(self):
        s = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3"
        self.assertEqual(19208, part_2_brute_force(s))

    def test_part_2_brute_force(self):
        with open("input.text") as f:
            self.assertEqual(24803586664192, part_2_brute_force(f.read()))

    def test_lengths(self):
        s = "3"
        self.assertEqual(1, part_2_brute_force(s))
        self.assertEqual(1, part_2(s))
        s = "3\n4"
        self.assertEqual(1, part_2_brute_force(s))
        self.assertEqual(1, part_2(s))
        s = "3\n4\n5"
        self.assertEqual(2, part_2_brute_force(s))
        self.assertEqual(2, part_2(s))
        s = "3\n4\n5\n6"
        self.assertEqual(4, part_2_brute_force(s))
        self.assertEqual(6, part_2(s))
        s = "3\n4\n5\n6\n7"
        self.assertEqual(7, part_2_brute_force(s))
        self.assertEqual(24, part_2(s))
        s = "3\n4\n5\n6\n7\n8"
        self.assertEqual(13, part_2_brute_force(s))
        self.assertEqual(120, part_2(s))
        s = "3\n4\n5\n6\n7\n8\n9"
        self.assertEqual(24, part_2_brute_force(s))
        self.assertEqual(720, part_2(s))
        s = "3\n4\n5\n6\n7\n8\n9\n10"
        self.assertEqual(44, part_2_brute_force(s))
        self.assertEqual(5040, part_2(s))

    def test_tribonacci(self):
        self.assertEqual(1, tribonacci_number(1))
        self.assertEqual(2, tribonacci_number(2))
        self.assertEqual(4, tribonacci_number(3))
        self.assertEqual(7, tribonacci_number(4))
        self.assertEqual(13, tribonacci_number(5))
        self.assertEqual(24, tribonacci_number(6))
        self.assertEqual(44, tribonacci_number(7))
        self.assertEqual(81, tribonacci_number(8))

    def test_example_3(self):
        s = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4"
        self.assertEqual(8, part_2(s))

    def test_example_4(self):
        s = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3"
        self.assertEqual(19208, part_2(s))

    # def test_part_2(self):
    #     with open("input.text") as f:
    #         self.assertEqual(2170, part_2(f.read()))


if __name__ == "__main__":
    unittest.main()
