import re

day_8_example = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


def jump_instructions(instructions: str) -> (int, int):
    instructions = instructions.strip('\n').split('\n')
    regex = re.compile(r"([\w]+) (inc|dec) (-?\d+) if (\w+) ([!<>=]+) (-?\d+)")
    highest_value = 0

    # Build registers
    registers = {}
    for line in instructions:
        r = line.split(' ')[0]
        registers[r] = 0

    for line in instructions:
        reg, inc, value, comp_reg, comp_op, comp_val = re.match(regex, line).groups()
        condition = "{} {} {}".format(registers[comp_reg], comp_op, comp_val)
        if eval(condition):
            if inc == "inc":
                registers[reg] += int(value)
            else:
                registers[reg] -= int(value)
            if registers[reg] > highest_value:
                highest_value = registers[reg]

    # print(registers)

    return max(registers.values()), highest_value


print(jump_instructions(day_8_example))
with open("day 8.input") as f:
    instructions = f.read()
print(jump_instructions(instructions))
