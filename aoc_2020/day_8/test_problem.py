import unittest

from aoc_2020.day_8.problem import *


class TestDay8(unittest.TestCase):

    def test_example_1(self):
        s = """
        nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6
        """
        with self.assertRaisesRegex(InfiniteLoopError, "5"):
            load_and_run(s)

    def test_part_1(self):
        with open("input.text") as f:
            with self.assertRaisesRegex(InfiniteLoopError, "2014"):
                load_and_run(f.read())

    def test_example_2(self):
        s = """
        nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6
        """
        self.assertEqual(8, fix_program(s))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(2251, fix_program(f.read()))


if __name__ == "__main__":
    unittest.main()
