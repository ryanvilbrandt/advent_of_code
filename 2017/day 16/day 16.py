import re
from typing import List

REG_SPIN = re.compile(r"s(\d+)")
REG_EXCHANGE = re.compile(r"x(\d+)/(\d+)")
REG_PARTNER = re.compile(r"p(\w+)/(\w+)")

def spin(array: List[str], length: int):
    return array[-1 * length:] + array[:-1 * length]


def exchange(array: List[str], a: int, b: int):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    return array


def partner(array: List[str], a: "str", b: "str"):
    x = array.index(a)
    y = array.index(b)
    return exchange(array, x, y)


def run_instruction(array: List[str], instruction: str):
    m = re.match(REG_SPIN, instruction)
    if m:
        return spin(array, int(m.group(1)))
    else:
        m = re.match(REG_EXCHANGE, instruction)
        if m:
            return exchange(array, int(m.group(1)), int(m.group(2)))
        else:
            m = re.match(REG_PARTNER, instruction)
            return partner(array, m.group(1), m.group(2))


def dance(dance_moves: str, array: str):
    array = [c for c in array]
    for line in dance_moves.strip('\n').split(','):
        # print("".join(array))
        array = run_instruction(array, line)
    return "".join(array)


# a = "s1,x3/4,pe/b"
# starting_array = "abcde"
# total_cycles = 21

with open("day 16.input") as f:
    a = f.read()
starting_array = "abcdefghijklmnop"
total_cycles = int(1e9)

# # Naive
# array = starting_array
# for i in range(total_cycles):
#     array = dance(a, array)
#     print(array)
#
# print("---------")

# Smart?
array = starting_array
cycle_count = 0
for i in range(total_cycles):
    if i % 10 == 0:
        print(f"{i}")
    array = dance(a, array)
    if array == starting_array:
        cycle_count = i + 1
        break

print(f"Cycle count: {cycle_count}")
array = starting_array
for i in range(total_cycles % cycle_count):
    array = dance(a, array)
print(array)