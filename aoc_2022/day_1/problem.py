from typing import List, Tuple


def group_by_elf(items: List[str]) -> List[List[int]]:
    elves = []
    elf = []
    for item in items:
        if not item:
            elves.append(elf)
            elf = []
        else:
            elf.append(int(item))
    elves.append(elf)
    return elves


def find_elf_with_most_calories(elves: List[List[int]]) -> Tuple[int, List[int]]:
    most_calories = 0
    swolest_elf = []
    for elf in elves:
        calories = sum(elf)
        if calories > most_calories:
            most_calories = calories
            swolest_elf = elf
    return most_calories, swolest_elf


def sort_elves(elves: List[List[int]]) -> List[List[int]]:
    return sorted(elves, key=lambda x: sum(x), reverse=True)


def sum_n_elves(elves: List[List[int]], n: int) -> int:
    elves_sublist = elves[:n]
    snacks = [snack for snacks in elves_sublist for snack in snacks]
    return sum(snacks)
