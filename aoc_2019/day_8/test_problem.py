import unittest

from aoc_2019.day_8.problem import *


class TestDay7(unittest.TestCase):

    def test_str_to_arrays(self):
        self.assertEqual(['123', '456'], str_to_arrays("123456", 3, 2))
        self.assertEqual(['12', '34', '56'], str_to_arrays("123456", 2, 3))
        self.assertEqual([['1', '3', '5'], ['2', '4', '6']], str_to_arrays_turned("123456", 3, 2))
        self.assertEqual([['1', '4'], ['2', '5'], ['3', '6']], str_to_arrays_turned("123456", 2, 3))

    def test_str_to_layers(self):
        self.assertEqual([['123', '456'], ['789', '012']], str_to_layers("123456789012", 3, 2))

    def test_check_image_1(self):
        s = "000122222" \
            "001122222" \
            "011111222" \
            "" \
            "000000122" \
            "000001122" \
            "000011222"
        self.assertEqual(8 * 13, check_image(s, 9, 3))

    def test_check_image_2(self):
        s = "000011222" \
            "000001122" \
            "000000122" \
            "" \
            "011222222" \
            "001111222" \
            "000111222"
        self.assertEqual(9 * 12, check_image(s, 9, 3))

    def test_part_1(self):
        with open("input.sif") as f:
            self.assertEqual(1677, check_image(f.read(), 25, 6))

    def test_merge_row_1(self):
        self.assertEqual("0101", merge_row("2121", "0000"))

    def test_merge_row_2(self):
        self.assertEqual("0010", merge_row("0022", "1110"))

    def test_merge_layer(self):
        base_layer = ["211", "121", "112"]
        new_layer = ["000", "000", "000"]
        self.assertEqual(["011", "101", "110"], merge_layer(base_layer, new_layer))

    def test_flatten_layers(self):
        layers = [
            ["212", "121", "212"],
            ["002", "020", "200"],
            ["000", "000", "000"]
        ]
        self.assertEqual(['010', '101', '010'], flatten_layers(layers))

    def test_flatten_image(self):
        image = "212121212" \
                "002020200" \
                "000000000"
        self.assertEqual(['010', '101', '010'], flatten_image(image, 3, 3))

    def test_part_2(self):
        with open("input.sif") as f:
            for row in increase_contrast(flatten_image(f.read(), 25, 6)):
                print(row)


if __name__ == "__main__":
    unittest.main()
