from typing import Tuple

DIRECTIONS = {
    "n": (0, +1, -1),
    "ne": (+1,  0, -1),
    "se": (+1, -1,  0),
    "s": (0, -1, +1),
    "sw": (-1,  0, +1),
    "nw": (-1, +1,  0)
}


def move(current_location: Tuple[int, int, int], direction: str) -> Tuple[int, int, int]:
    """
    :param current_location: 3-tuple of ints
    :param direction: One of the keys in DIRECTIONS
    :return: New 3-tuple of ints
    """
    t = DIRECTIONS[direction]
    return (
        t[0] + current_location[0],
        t[1] + current_location[1],
        t[2] + current_location[2],
    )


def get_max_distance(current_location: Tuple[int, int, int]):
    return max([abs(x) for x in current_location])


def walk(directions: str, current_location=(0, 0, 0)):
    # print()
    # print(directions)
    direction_list = directions.split(',')
    max_total_distance = 0
    for d in direction_list:
        current_location = move(current_location, d)
        if get_max_distance(current_location) > max_total_distance:
            max_total_distance = get_max_distance(current_location)
        # print(current_location)
    # Find distance
    return get_max_distance(current_location), max_total_distance


print(walk("ne,ne,ne"))
print(walk("ne,ne,sw,sw"))
print(walk("ne,ne,s,s"))
print(walk("se,sw,se,sw,sw"))
with open("day 11.input") as f:
    print(walk(f.read()))