import unittest

from aoc_2020.day_6.problem import *

EXAMPLE = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestDay6(unittest.TestCase):

#     def test_get_all_yes_answers(self):
#         self.assertEqual(3, get_all_yes_answers("a\nb\nc"))
#         self.assertEqual(6, get_all_yes_answers("""abcx
# abcy
# abcz"""))
# 
#     def test_get_all_answer_counts(self):
#         self.assertEqual(
#             [3, 3, 3, 1, 1],
#             get_all_answer_counts(EXAMPLE)
#         )
# 
#     def test_example_1(self):
#         self.assertEqual(11, sum_answer_counts(EXAMPLE))
# 
#     def test_part_1(self):
#         with open("input.text") as f:
#             self.assertEqual(6683, sum_answer_counts(f.read()))

    def test_get_all_yes_answers_part_2(self):
        self.assertEqual(0, get_all_yes_answers("a\nb\nc"))
        self.assertEqual(3, get_all_yes_answers("""abcx
abcy
abcz"""))

    def test_example_2(self):
        self.assertEqual(6, sum_answer_counts(EXAMPLE))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(3122, sum_answer_counts(f.read()))


if __name__ == "__main__":
    unittest.main()
