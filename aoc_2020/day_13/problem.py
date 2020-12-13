import math
import re
from enum import Enum
from math import inf
from time import time
from typing import Tuple, NamedTuple

from aoc_2020.common import text_to_list


def get_wait_time(epoch: int, bus_number: int) -> int:
    return (epoch // bus_number + 1) * bus_number - epoch


def part_1(note):
    line_1, line_2 = text_to_list(note)
    epoch = int(line_1)
    bus_schedule = line_2.split(",")
    minimum_wait_time = inf
    minimum_wait_time_bus = -1
    for bus_number in bus_schedule:
        if bus_number == "x":
            continue
        wait_time = get_wait_time(epoch, int(bus_number))
        if wait_time < minimum_wait_time:
            minimum_wait_time, minimum_wait_time_bus = wait_time, bus_number
    return minimum_wait_time * int(minimum_wait_time_bus)


def check_time_for_departure(epoch: int, bus_number: int) -> bool:
    return epoch % bus_number == 0


def part_2(note):
    line_1, line_2 = text_to_list(note)
    bus_schedule = line_2.split(",")
    numbers_to_check = []
    for i, bus_number in enumerate(bus_schedule):
        if bus_number == "x":
            continue
        numbers_to_check.append((int(bus_number), i))

    epoch = 0
    increment = numbers_to_check[0][0]
    for bus_number, offset in numbers_to_check:
        while (epoch + offset) % bus_number != 0:
            epoch += increment
        increment = (bus_number * increment) // math.gcd(increment, bus_number)
    return epoch
