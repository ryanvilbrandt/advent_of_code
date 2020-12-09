from itertools import combinations
from typing import Set, List, Iterable

from aoc_2020.common import text_to_list


def get_all_sums(num_list: Iterable[int]) -> Set[int]:
    return set(map(lambda x: x[0] + x[1], combinations(num_list, r=2)))


def find_invalid_number(num_list: List[int], preamble_length=25):
    for i in range(preamble_length, len(num_list)):
        sums = get_all_sums(num_list[i - preamble_length:i])
        if num_list[i] not in sums:
            return num_list[i]


def load_and_find_invalid_number(s: str, preamble_length=25):
    num_list = list(map(int, text_to_list(s)))
    return find_invalid_number(num_list, preamble_length)


def find_contiguous_numbers(num_list: List[int], target_number: int) -> List[int]:
    for i in range(1, len(num_list)):
        for j in range(len(num_list) - i):
            if sum(num_list[j:i]) == target_number:
                return num_list[j:i]


def part_2(s, preamble_length=25):
    num_list = list(map(int, text_to_list(s)))
    invalid_number = find_invalid_number(num_list, preamble_length)
    contiguous_nums = find_contiguous_numbers(num_list, invalid_number)
    return min(contiguous_nums) + max(contiguous_nums)
