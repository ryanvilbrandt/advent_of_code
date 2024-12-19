import re


def sum_mul_instructions(s: str) -> int:
    p = r"mul\((\d+),(\d+)\)"
    sum = 0
    for m in re.finditer(p, s):
        sum += int(m.group(1)) * int(m.group(2))
    return sum


def sum_mul_instructions_w_do_dont(s: str) -> int:
    p = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    sum = 0
    enabled = True
    for m in re.finditer(p, s):
        if m.group() == "do()":
            enabled = True
        elif m.group() == "don't()":
            enabled = False
        elif enabled:
            sum += int(m.group(1)) * int(m.group(2))
    return sum
