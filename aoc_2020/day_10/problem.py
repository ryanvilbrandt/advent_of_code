from functools import lru_cache
from math import factorial
from typing import Iterable

from aoc_2020.common import text_to_list


def get_differences(num_list: Iterable[int]):
    differences = []
    sorted_list = sorted(num_list)
    sorted_list.insert(0, 0)
    for i in range(len(sorted_list) - 1):
        differences.append(sorted_list[i + 1] - sorted_list[i])
    differences.append(3)
    return differences


def checksum_differences(differences):
    assert differences.count(2) == 0
    return differences.count(3) * differences.count(1)


def part_1(text):
    differences = get_differences(map(int, text_to_list(text)))
    return checksum_differences(differences)


num_set = set()
def count_arrangements_brute_force(num_list: Iterable[int]):
    global num_set
    num_set = set(num_list)
    max_num = max(num_set)
    return count_arrangements_recurse(0, max_num)


@lru_cache
def count_arrangements_recurse(start_num: int, max_num: int) -> int:
    global num_set
    if start_num == max_num:
        return 1
    arrangement_count = 0
    for i in range(start_num + 1, start_num + 4):
        if i in num_set:
            arrangement_count += count_arrangements_recurse(i, max_num)
    return arrangement_count


def part_2_brute_force(text):
    return count_arrangements_brute_force(map(int, text_to_list(text)))


def tribonacci_number(n):
    if n < 1:
        return 1
    a, b, c = 0, 0, 1
    for i in range(n):
        total = a + b + c
        a = b
        b = c
        c = total
    return c


def count_arrangements(num_list: Iterable[int]):
    total_arrangements = 0
    run_length = 0
    last_num = None
    for n in num_list:
        if last_num is None:
            last_num = n
            continue
        if n == last_num + 1:
            run_length += 1
        else:
            total_arrangements += tribonacci_number(run_length)
            run_length = 0
        last_num = n
    total_arrangements += factorial(run_length)
    return total_arrangements


def part_2(text):
    return count_arrangements(map(int, text_to_list(text)))
