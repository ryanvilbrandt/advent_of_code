import re
from enum import Enum
from typing import Tuple, NamedTuple

from aoc_2020.common import text_to_list


class Coords(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    NORTH = Coords(0, -1)
    EAST = Coords(+1, 0)
    SOUTH = Coords(0, +1)
    WEST = Coords(-1, 0)


def turn(direction: Direction, turn_angle: int) -> Direction:
    directions_list = list(Direction)
    return directions_list[(directions_list.index(direction) + turn_angle // 90) % 4]


def move(coords: Coords, direction: Direction, value: int):
    return Coords(coords.x + direction.value.x * value, coords.y + direction.value.y * value)


def run_instruction_part_1(coords: Coords, direction: Direction, instruction: str) -> Tuple[Coords, Direction]:
    m = re.match(r"(\w)(\d+)", instruction)
    opcode, value = m.group(1), int(m.group(2))
    if opcode == "L":
        direction = turn(direction, value * -1)
    elif opcode == "R":
        direction = turn(direction, value)
    else:
        if opcode == "F":
            move_direction = direction
        elif opcode == "N":
            move_direction = Direction.NORTH
        elif opcode == "E":
            move_direction = Direction.EAST
        elif opcode == "S":
            move_direction = Direction.SOUTH
        elif opcode == "W":
            move_direction = Direction.WEST
        else:
            raise ValueError(opcode)
        coords = move(coords, move_direction, value)
    # print(instruction, coords, direction)
    return coords, direction


def run_instructions_part_1(text):
    instructions_list = text_to_list(text)
    coords = Coords(0, 0)
    direction = Direction.EAST
    for instruction in instructions_list:
        coords, direction = run_instruction_part_1(coords, direction, instruction)
    return abs(coords.x) + abs(coords.y)


def turn_waypoint(waypoint, turn_angle):
    if turn_angle == 90 or turn_angle == -270:
        return Coords(waypoint.y * -1, waypoint.x)
    if turn_angle == 180 or turn_angle == -180:
        return Coords(waypoint.x * -1, waypoint.y * -1)
    if turn_angle == 270 or turn_angle == -90:
        return Coords(waypoint.y, waypoint.x * -1)


def run_instruction_part_2(ship: Coords, waypoint: Coords, instruction: str) -> Tuple[Coords, Coords]:
    m = re.match(r"(\w)(\d+)", instruction)
    opcode, value = m.group(1), int(m.group(2))
    if opcode == "F":
        ship = Coords(ship.x + waypoint.x * value, ship.y + waypoint.y * value)
    elif opcode == "L":
        waypoint = turn_waypoint(waypoint, value * -1)
    elif opcode == "R":
        waypoint = turn_waypoint(waypoint, value)
    else:
        if opcode == "N":
            move_direction = Direction.NORTH
        elif opcode == "E":
            move_direction = Direction.EAST
        elif opcode == "S":
            move_direction = Direction.SOUTH
        elif opcode == "W":
            move_direction = Direction.WEST
        else:
            raise ValueError(opcode)
        waypoint = move(waypoint, move_direction, value)
    # print(instruction, ship, waypoint)
    return ship, waypoint


def run_instructions_part_2(text):
    instructions_list = text_to_list(text)
    coords = Coords(0, 0)
    waypoint = Coords(10, -1)
    for instruction in instructions_list:
        coords, waypoint = run_instruction_part_2(coords, waypoint, instruction)
    return abs(coords.x) + abs(coords.y)
