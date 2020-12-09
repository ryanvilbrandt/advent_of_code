import re
from typing import Tuple, List, NamedTuple

from aoc_2020.common import text_to_list


class Instruction(NamedTuple):
    op: str
    val: int


class InfiniteLoopError(Exception):
    pass


accumulator = 0


def perform_instruction(instruction: Instruction) -> int:
    global accumulator
    if instruction.op == "jmp":
        return instruction.val
    if instruction.op == "nop":
        pass
    elif instruction.op == "acc":
        accumulator += instruction.val
    return 1


def run_program(instructions_list: List[Instruction]) -> int:
    global accumulator
    past_ptrs = set()
    ptr = 0
    accumulator = 0
    while ptr < len(instructions_list):
        past_ptrs.add(ptr)
        ptr += perform_instruction(instructions_list[ptr])
        if ptr in past_ptrs:
            raise InfiniteLoopError(accumulator)
    return accumulator


def load_program(instructions_text: str) -> List[Instruction]:
    instructions_list = []
    for instruction in text_to_list(instructions_text):
        m = re.search(r"([a-z]{3}) ([+\-]\d+)", instruction)
        instructions_list.append(Instruction(m.group(1), int(m.group(2))))
    return instructions_list


def load_and_run(instructions_text: str) -> int:
    instructions_list = load_program(instructions_text)
    return run_program(instructions_list)


def fix_program(instructions_text: str):
    instructions_list = load_program(instructions_text)
    for i, x in enumerate(instructions_list):
        if x.op == "nop":
            new_instruction = "jmp"
        elif x.op == "jmp":
            new_instruction = "nop"
        else:
            continue
        instructions_list_copy = instructions_list[:]
        instructions_list_copy[i] = Instruction(new_instruction, x.val)
        try:
            acc = run_program(instructions_list_copy)
            return acc
        except InfiniteLoopError:
            pass
