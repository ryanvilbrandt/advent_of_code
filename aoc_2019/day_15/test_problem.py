import unittest
from unittest import mock
from unittest.mock import patch, MagicMock

from aoc_2019.day_15.problem import *

EXAMPLE_1_OUTPUT = """ ## 
#..#
D.# 
 #  """


class TestDay15(unittest.TestCase):

    def test_Direction(self):
        robot = Robot()
        s = "##.\n" \
            "#DO\n" \
            "  ."
        robot.grid[(0, 0)] = RoomObject.FLOOR
        robot.grid[(-1, -1)] = RoomObject.WALL
        robot.grid[(-1, 0)] = RoomObject.WALL
        robot.grid[(0, -1)] = RoomObject.WALL
        robot.grid[(1, -1)] = RoomObject.FLOOR
        robot.grid[(1, 0)] = RoomObject.OXYGEN_SYSTEM
        robot.grid[(1, 1)] = RoomObject.FLOOR
        self.assertEqual(s, robot.get_grid())

    def test_attempt_move(self):
        robot = Robot()
        self.assertEqual([0, -1], robot.attempt_move(Direction.NORTH))
        self.assertEqual([0, 1], robot.attempt_move(Direction.SOUTH))
        self.assertEqual([-1, 0], robot.attempt_move(Direction.WEST))
        self.assertEqual([1, 0], robot.attempt_move(Direction.EAST))

    def test_move(self):
        robot = Robot()
        m = MagicMock()
        robot.intcode = m
        m.run.return_value = RoomObject.WALL.value
        self.assertEqual(RoomObject.WALL, robot.move(Direction.NORTH))
        self.assertEqual("#\nD", robot.get_grid())
        m.run.return_value = RoomObject.OXYGEN_SYSTEM.value
        self.assertEqual(RoomObject.OXYGEN_SYSTEM, robot.move(Direction.EAST))
        m.run.return_value = RoomObject.FLOOR.value
        self.assertEqual(RoomObject.FLOOR, robot.move(Direction.NORTH))
        self.assertEqual("#D\n.O", robot.get_grid())

    def test_example_1_get_grid(self):
        moves = [
            (Direction.NORTH, RoomObject.WALL),
            (Direction.EAST, RoomObject.FLOOR),
            (Direction.NORTH, RoomObject.WALL),
            (Direction.SOUTH, RoomObject.WALL),
            (Direction.EAST, RoomObject.WALL),
            (Direction.WEST, RoomObject.FLOOR),
            (Direction.WEST, RoomObject.WALL),
            (Direction.SOUTH, RoomObject.FLOOR),
            (Direction.SOUTH, RoomObject.WALL),
            (Direction.WEST, RoomObject.OXYGEN_SYSTEM),
        ]
        robot = Robot()
        m = MagicMock()
        robot.intcode = m
        for direction, output in moves:
            m.run.return_value = output.value
            self.assertEqual(output, robot.move(direction))
        self.assertEqual(EXAMPLE_1_OUTPUT, robot.get_grid())

    def test_example_1(self):
        robot = Robot(use_curses=True)
        with open("aoc_2019/day_15/input.text") as f:
            robot.run_intcode(f.read())

    def test_pick_next_direction(self):
        robot = Robot()
        self.assertEqual(Direction.NORTH, robot.pick_next_direction())
        robot.grid[tuple(robot.attempt_move(Direction.NORTH))] = RoomObject.WALL
        self.assertEqual(Direction.EAST, robot.pick_next_direction())
        robot.grid[tuple(robot.attempt_move(Direction.EAST))] = RoomObject.WALL
        self.assertEqual(Direction.SOUTH, robot.pick_next_direction())
        robot.grid[tuple(robot.attempt_move(Direction.SOUTH))] = RoomObject.WALL
        self.assertEqual(Direction.WEST, robot.pick_next_direction())


if __name__ == "__main__":
    unittest.main()
