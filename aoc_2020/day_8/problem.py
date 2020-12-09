import re
from typing import Tuple, List

from aoc_2020.common import text_to_list


class InfiniteLoopError(Exception):
    pass


accumulator = 0


def perform_instruction(instruction: Tuple[str, int]) -> int:
    global accumulator
    if instruction[0] == "jmp":
        return instruction[1]
    if instruction[0] == "nop":
        pass
    elif instruction[0] == "acc":
        accumulator += instruction[1]
    return 1


def run_program(instructions_list: List[Tuple[str, int]]) -> int:
    global accumulator
    past_ptrs = []
    ptr = 0
    accumulator = 0
    while ptr < len(instructions_list):
        past_ptrs.append(ptr)
        ptr += perform_instruction(instructions_list[ptr])
        if ptr in past_ptrs:
            raise InfiniteLoopError(accumulator)
    return accumulator


def load_program(instructions_text: str) -> List[Tuple[str, int]]:
    instructions_list = []
    for instruction in text_to_list(instructions_text):
        m = re.search(r"([a-z]{3}) ([+\-]\d+)", instruction)
        instructions_list.append((m.group(1), int(m.group(2))))
    return instructions_list


def load_and_run(instructions_text: str) -> int:
    instructions_list = load_program(instructions_text)
    return run_program(instructions_list)


def fix_program(instructions_text: str):
    instructions_list = load_program(instructions_text)
    for i, x in enumerate(instructions_list):
        if x[0] == "nop":
            new_instruction = "jmp"
        elif x[0] == "jmp":
            new_instruction = "nop"
        else:
            continue
        instructions_list_copy = instructions_list[:]
        instructions_list_copy[i] = (new_instruction, x[1])
        try:
            acc = run_program(instructions_list_copy)
            return acc
        except InfiniteLoopError:
            pass
