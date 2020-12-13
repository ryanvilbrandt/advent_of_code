import unittest

from aoc_2020.day_13.problem import *


class TestDay13(unittest.TestCase):

    def test_get_wait_time(self):
        self.assertEqual(6, get_wait_time(939, 7))
        self.assertEqual(10, get_wait_time(939, 13))
        self.assertEqual(5, get_wait_time(939, 59))

    def test_example_1(self):
        s = """
        939
        7,13,x,x,59,x,31,19
        """
        self.assertEqual(295, part_1(s))

    def test_part_1(self):
        with open("input.text") as f:
            self.assertEqual(246, part_1(f.read()))

    def test_example_2(self):
        s = """
        939
        7,13,x,x,59,x,31,19
        """
        self.assertEqual(1068781, part_2(s))

    def test_example_3(self):
        s = """
        939
        17,x,13,19
        """
        self.assertEqual(3417, part_2(s))

    def test_example_4(self):
        s = """
        939
        67,7,59,61
        """
        self.assertEqual(754018, part_2(s))

    def test_example_5(self):
        s = """
        939
        67,x,7,59,61
        """
        self.assertEqual(779210, part_2(s))

    def test_example_6(self):
        s = """
        939
        67,7,x,59,61
        """
        self.assertEqual(1261476, part_2(s))

    def test_example_7(self):
        s = """
        939
        1789,37,47,1889
        """
        self.assertEqual(1202161486, part_2(s))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(939490236001473, part_2(f.read()))


if __name__ == "__main__":
    unittest.main()
