import unittest

from aoc_2020.day_2.problem import *


class TestDay2(unittest.TestCase):

    def test_example_1(self):
        text = """
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        """
        self.assertEqual(2, check_passwords_part_1(text))

    def test_part_1(self):
        with open("input.text") as f:
            print(check_passwords_part_1(f.read()))

    def test_example_2(self):
        text = """
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        """
        self.assertEqual(1, check_passwords_part_2(text))

    def test_part_2(self):
        with open("input.text") as f:
            print(check_passwords_part_2(f.read()))


if __name__ == "__main__":
    unittest.main()
