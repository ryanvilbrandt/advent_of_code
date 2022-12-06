import re
from typing import List, Tuple

from aoc_2022.common import text_to_list


def text_to_assignments(text: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    m = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def is_complete_overlap(text: str) -> bool:
    first, second = text_to_assignments(text)
    if first[0] <= second[0] and first[1] >= second[1]:
        return True
    return first[0] >= second[0] and first[1] <= second[1]


def count_complete_overlaps(text: str) -> int:
    lines = text_to_list(text)
    return len([line for line in lines if is_complete_overlap(line)])


def is_partial_overlap(text: str) -> int:
    first, second = text_to_assignments(text)
    first_set = set(range(first[0], first[1] + 1))
    second_set = set(range(second[0], second[1] + 1))
    return bool(first_set.intersection(second_set))


def count_partial_overlaps(text: str) -> int:
    lines = text_to_list(text)
    return len([line for line in lines if is_partial_overlap(line)])
