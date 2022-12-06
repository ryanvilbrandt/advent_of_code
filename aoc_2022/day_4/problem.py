import re
from typing import List, Tuple

from aoc_2022.common import text_to_list


def text_to_assignments(text: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    m = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def is_complete_overlap(text: str) -> bool:
    s1, s2 = text_to_assignments(text)
    return (s1[0] <= s2[0] <= s1[1] and s1[0] <= s2[1] <= s1[1]) or \
           (s2[0] <= s1[0] <= s2[1] and s2[0] <= s1[1] <= s2[1])


def count_complete_overlaps(text: str) -> int:
    lines = text_to_list(text)
    return len([line for line in lines if is_complete_overlap(line)])


def is_partial_overlap(text: str) -> int:
    s1, s2 = text_to_assignments(text)
    return (s1[0] <= s2[0] <= s1[1] or s1[0] <= s2[1] <= s1[1]) or \
           (s2[0] <= s1[0] <= s2[1] or s2[0] <= s1[1] <= s2[1])


def count_partial_overlaps(text: str) -> int:
    lines = text_to_list(text)
    return len([line for line in lines if is_partial_overlap(line)])
