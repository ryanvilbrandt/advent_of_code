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

    def test_print_screen_1(self):
        ag = ArcadeGame("99")
        ag.create_tile(2, 2, 0)
        ag.create_tile(3, 2, 1)
        ag.create_tile(2, 3, 2)
        ag.create_tile(3, 3, 3)
        ag.create_tile(2, 4, 4)
        ag.print_screen()

    def test_print_screen_2(self):
        ag = ArcadeGame("99")
        ag.create_tile(0, 0, Tile.WALL)
        ag.create_tile(1, 0, Tile.WALL)
        ag.create_tile(2, 0, Tile.WALL)
        ag.create_tile(3, 0, Tile.WALL)
        ag.create_tile(4, 0, Tile.WALL)

        ag.create_tile(0, 1, Tile.WALL)
        ag.create_tile(1, 1, Tile.BLOCK)
        ag.create_tile(2, 1, Tile.BLOCK)
        ag.create_tile(3, 1, Tile.BLOCK)
        ag.create_tile(4, 1, Tile.WALL)

        ag.create_tile(0, 2, Tile.WALL)
        ag.create_tile(1, 2, Tile.BLOCK)
        ag.create_tile(2, 2, Tile.BLOCK)
        ag.create_tile(3, 2, Tile.BLOCK)
        ag.create_tile(4, 2, Tile.WALL)

        ag.create_tile(0, 3, Tile.WALL)
        ag.create_tile(2, 3, Tile.BALL)
        ag.create_tile(4, 3, Tile.WALL)

        ag.create_tile(0, 4, Tile.WALL)
        ag.create_tile(2, 4, Tile.HORIZONTAL_PADDLE)
        ag.create_tile(4, 4, Tile.WALL)

        ag.print_screen()

    @unittest.skip
    def test_print_screen_3(self):
        with open("input.text") as f:
            ag = ArcadeGame(f.read())
        ag.start_game()
        ag.print_screen()

    def test_day_13_part_2(self):
        with open("input.text") as f:
            ag = ArcadeGame(f.read())
        ag.start_game(add_quarter=True)
        self.assertEqual(10547, ag.score)


if __name__ == "__main__":
    unittest.main()
