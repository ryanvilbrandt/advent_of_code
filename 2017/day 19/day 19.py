from re import match
from typing import List


def get_start(mymap: List[str]):
    for i, c in enumerate(mymap[0]):
        if c == "|":
            return i
    raise Exception("No map start found at the top of the map")


def map_step(x: int, y: int, direction):
    if direction == "north":
        return x, y - 1
    if direction == "east":
        return x + 1, y
    if direction == "south":
        return x, y + 1
    if direction == "west":
        return x - 1, y
    raise Exception(f"Invalid direction: {direction}")


def check_location(mymap: List[str], x: int, y: int) -> str:
    if x < 0 or y < 0:
        return ""
    try:
        char = mymap[y][x]
    except IndexError:
        return ""
    if char in ('|', '-'):
        return "path"
    if char == '+':
        return "corner"
    if char == " ":
        return "empty"
    if match(r"\w", char):
        return "letter"
    raise Exception(f"Unknown character at {x}, {y}: {char}")


def turn_corner(mymap, x, y, current_dir):
    """
    Three assumptions are made when we get to every corner:
    1) Every corner has two paths connected to it (a path can be represented by a line or a letter)
    2) No corner has a path adjacent to it that doesn't connect to that corner
    3) We always enter from one of the paths, and must leave by the only remaining path
    :param mymap:
    :param x:
    :param y:
    :param current_dir:
    :return:
    """
    if not current_dir == "north":
        # If not coming from the south, check the southern cell
        if check_location(mymap, x, y + 1) in ("path", "letter"):
            return "south"
    if not current_dir == "south":
        # If not coming from the north, check the northern cell
        if check_location(mymap, x, y - 1) in ("path", "letter"):
            return "north"
    if not current_dir == "east":
        # If not coming from the west, check the western cell
        if check_location(mymap, x - 1, y) in ("path", "letter"):
            return "west"
    if not current_dir == "west":
        # If not coming from the east, check the eastern cell
        if check_location(mymap, x + 1, y) in ("path", "letter"):
            return "east"


def walk_map(mymap: str):
    mymap = mymap.strip('\n').split('\n')

    x, y = get_start(mymap), 0
    direction = "south"
    letter_list = ""
    steps = 0

    while True:
        location = check_location(mymap, x, y)
        print(f"{mymap[y][x]} {x} {y}")
        if location == "":
            print(f"We've left the map! {x} {y} | {letter_list} | {steps}")
        elif location == "empty":
            print(f"We left the path! {x} {y} | {letter_list} | {steps}")
            return
        elif location == "path":
            pass
        elif location == "letter":
            letter_list += mymap[y][x]
        elif location == "corner":
            direction = turn_corner(mymap, x, y, direction)
        else:
            raise Exception(f"Unknown node at {x}, {y}")
        x, y = map_step(x, y, direction)
        steps += 1


# a = """
#      |
#      |  +--+
#      A  |  C
#  F---|----E|--+
#      |  |  |  D
#      +B-+  +--+
# """
with open("day 19.input") as f:
    a = f.read()

walk_map(a)
