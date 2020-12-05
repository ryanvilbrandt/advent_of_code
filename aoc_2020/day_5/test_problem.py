import unittest

from aoc_2020.day_5.problem import *


class TestDay5(unittest.TestCase):

    def test_get_seat_id(self):
        self.assertEqual(357, get_seat_id("FBFBBFFRLR"))
        self.assertEqual(567, get_seat_id("BFFFBBFRRR"))
        self.assertEqual(119, get_seat_id("FFFBBBFRRR"))
        self.assertEqual(820, get_seat_id("BBFFBBFRLL"))

    def test_get_highest_seat_id(self):
        boarding_passes = """
        FBFBBFFRLR
        BFFFBBFRRR
        FFFBBBFRRR
        BBFFBBFRLL
        """
        min_seat_id, max_seat_id = get_highest_and_lowest_seat_id(boarding_passes)
        self.assertEqual(119, min_seat_id)
        self.assertEqual(820, max_seat_id)

    def test_part_1(self):
        with open("input.text") as f:
            min_seat_id, max_seat_id = get_highest_and_lowest_seat_id(f.read())
            self.assertEqual(38, min_seat_id)
            self.assertEqual(998, max_seat_id)

    def test_expected_total(self):
        self.assertEqual(5050, get_expected_total(1, 100))
        self.assertEqual(45, get_expected_total(5, 10))

    def test_part_2(self):
        with open("input.text") as f:
            self.assertEqual(676, get_missing_seat(f.read()))


if __name__ == "__main__":
    unittest.main()
