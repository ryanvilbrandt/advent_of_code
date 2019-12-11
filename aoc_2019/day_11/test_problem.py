import unittest

from aoc_2019.day_11.problem import *


class TestDay10(unittest.TestCase):

    def test_Direction(self):
        direction = Direction.UP
        self.assertEqual(direction, Direction.UP)
        direction = direction.turn_left()
        self.assertEqual(direction, Direction.LEFT)
        direction = direction.turn_right()
        direction = direction.turn_right()
        self.assertEqual(direction, Direction.RIGHT)
        direction = direction.turn_right()
        self.assertEqual(direction, Direction.DOWN)

    def test_Robot_init(self):
        robot = Robot([0, 0])
        self.assertEqual([0, 0], robot.coords)
        self.assertEqual(Direction.UP, robot.direction)
        self.assertEqual(Color.BLACK, robot.grid[(0, 0)])

    def test_get_current_color(self):
        robot = Robot([0, 0])
        self.assertEqual(Color.BLACK, robot.get_current_color())

    def test_paint(self):
        robot = Robot([0, 0])
        self.assertEqual(Color.BLACK, robot.get_current_color())
        robot.paint(0)
        self.assertEqual(Color.BLACK, robot.get_current_color())
        robot.paint(1)
        self.assertEqual(Color.WHITE, robot.get_current_color())
        robot.paint(1)
        self.assertEqual(Color.WHITE, robot.get_current_color())
        robot.paint(0)
        self.assertEqual(Color.BLACK, robot.get_current_color())

    def test_move(self):
        robot = Robot([0, 0])
        self.assertEqual([0, 0], robot.coords)
        self.assertEqual(Direction.UP, robot.direction)
        robot.move()
        self.assertEqual([0, 1], robot.coords)
        self.assertEqual(Direction.UP, robot.direction)
        robot.turn(1)
        robot.move()
        self.assertEqual([1, 1], robot.coords)
        self.assertEqual(Direction.RIGHT, robot.direction)
        robot.turn(1)
        robot.move()
        self.assertEqual([1, 0], robot.coords)
        self.assertEqual(Direction.DOWN, robot.direction)
        robot.turn(0)
        robot.move()
        self.assertEqual([2, 0], robot.coords)
        self.assertEqual(Direction.RIGHT, robot.direction)
        robot.turn(1)
        robot.move()
        self.assertEqual([2, -1], robot.coords)
        self.assertEqual(Direction.DOWN, robot.direction)
        robot.turn(1)
        robot.move()
        self.assertEqual([1, -1], robot.coords)
        self.assertEqual(Direction.LEFT, robot.direction)
        robot.turn(1)
        robot.move()
        self.assertEqual([1, 0], robot.coords)
        self.assertEqual(Direction.UP, robot.direction)

    def test_run_intcode(self):
        robot = Robot([0, 0])
        halted_intcode = robot.run_intcode("3,1,104,1,104,1,99")
        self.assertEqual(0, halted_intcode.tape[1])
        self.assertEqual(Color.WHITE, robot.grid[(0, 0)])
        self.assertEqual(Direction.RIGHT, robot.direction)
        robot.print_grid()

    def test_day_10_example_1(self):
        robot = Robot([2, 2])
        program = "104,1,104,0,104,0,104,0,104,1,104,0,104,1,104,0,104,0,104,1,104,1,104,0,104,1,104,0,99"
        robot.run_intcode(program)
        self.assertEqual([2, 1], robot.coords)
        self.assertEqual(Direction.LEFT, robot.direction)
        self.assertEqual({
            (2, 2): Color.BLACK,
            (1, 2): Color.BLACK,
            (1, 3): Color.WHITE,
            (2, 3): Color.WHITE,
            (3, 2): Color.WHITE,
            (3, 1): Color.WHITE,
            (2, 1): Color.BLACK
        }, robot.grid)
        self.assertEqual(6, robot.count_panels_painted())
        robot.print_grid()

    def test_day_10_part_1(self):
        robot = Robot([0, 0])
        with open("input.text") as f:
            robot.run_intcode(f.read())
        self.assertEqual(1885, robot.count_panels_painted())
        robot.print_grid()

    def test_day_10_part_2(self):
        robot = Robot([0, 0])
        robot.grid[(0, 0)] = Color.WHITE
        with open("input.text") as f:
            robot.run_intcode(f.read())
        self.assertEqual(249, robot.count_panels_painted())
        robot.print_grid()


if __name__ == "__main__":
    unittest.main()
