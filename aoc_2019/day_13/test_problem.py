import unittest

from aoc_2019.day_13.problem import *


class TestDay10(unittest.TestCase):

    def test_create_tile(self):
        ag = ArcadeGame("99")
        ag.create_tile(1, 2, 3)
        ag.create_tile(6, 5, 4)
        self.assertEqual(
            {
                (1, 2): Tile.HORIZONTAL_PADDLE,
                (6, 5): Tile.BALL
            }, ag.grid
        )

    def test_get_tile_count(self):
        ag = ArcadeGame("99")
        ag.create_tile(1, 2, 3)
        ag.create_tile(6, 5, 4)
        ag.create_tile(7, 8, 2)
        ag.create_tile(7, 8, 4)
        self.assertEqual({Tile.HORIZONTAL_PADDLE: 1, Tile.BALL: 2}, ag.get_tile_count())

    def test_run_intcode(self):
        ag = ArcadeGame("104,1,104,2,104,3,104,6,104,5,104,4,104,7,104,8,104,4,99")
        ag.start_game()
        self.assertEqual(
            {
                (1, 2): Tile.HORIZONTAL_PADDLE,
                (6, 5): Tile.BALL,
                (7, 8): Tile.BALL
            }, ag.grid
        )

    def test_day_13_part_1(self):
        with open("input.text") as f:
            ag = ArcadeGame(f.read())
        ag.start_game()
        self.assertEqual(
            {
                Tile.EMPTY: 603,
                Tile.WALL: 82,
                Tile.BLOCK: 193,
                Tile.HORIZONTAL_PADDLE: 1,
                Tile.BALL: 1
            }, ag.get_tile_count()
        )


if __name__ == "__main__":
    unittest.main()
