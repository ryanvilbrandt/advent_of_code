from typing import List, Tuple

from aoc_2022.common import text_to_list


def find_common_items(text: str) -> List[str]:
    lines = text_to_list(text)
    return [find_common_item(line) for line in lines]


def find_common_item(line: str) -> str:
    assert len(line) % 2 == 0
    first_compartment = line[:len(line) // 2]
    second_compartment = line[len(line) // 2:]
    assert len(first_compartment) == len(second_compartment)
    item_set = set(first_compartment).intersection(second_compartment)
    assert len(item_set) == 1
    return item_set.pop()


def get_total_priority(items: List[str]) -> int:
    return sum(get_priority(item) for item in items)


def get_priority(s: str) -> int:
    o = ord(s)
    if o > ord("a"):
        return o - ord("a") + 1
    return o - ord("A") + 27


def find_badges(text: str, group_size: int = 3) -> List[str]:
    lines = list(text_to_list(text))
    badges = []
    for i in range(0, len(lines), group_size):
        badges.append(find_badge(lines[i:i + group_size]))
    return badges


def find_badge(rucksacks: List[str]) -> str:
    final_set = None
    for rucksack in rucksacks:
        if final_set is None:
            final_set = set(rucksack)
            continue
        final_set = final_set.intersection(rucksack)
    assert len(final_set) == 1
    return final_set.pop()
