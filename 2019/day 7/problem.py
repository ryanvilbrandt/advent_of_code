import time
from enum import Enum
from typing import List, Union


class Mode(Enum):
    POSITIONAL = 0
    IMMEDIATE = 1


AMP_MODE_BASE = 5
MAX_AMP_MODE = 5**5 - 1


class IntCode:

    def __init__(self, tape: str, input_buffer: List[int]=None):
        self.tape = [int(i.strip()) for i in tape.split(',')]
        self.index = 0
        self.diagnostic_code = 0
        self.last_instructions = []
        self.input_buffer = input_buffer if input_buffer is not None else []

    def run(self):
        self.index = 0
        while True:
            # self.print_tape()
            if self.tape[self.index] == 99:
                return self.diagnostic_code
            if self.diagnostic_code != 0:
                raise DiagnosticCodeError(
                    self.diagnostic_code,
                    self.tape,
                    self.last_instructions
                )
            self.instruction()
            # time.sleep(1)

    def print_tape(self):
        print(self.tape)
        indent = sum([len(str(i) + ", ") for i in self.tape[:self.index + 1]]) - 2
        print(indent * " " + "^")

    def instruction(self):
        operation, mode_map = self.tape[self.index] % 100, self.tape[self.index] // 100
        func = self.operations.get(operation)
        if func is None:
            raise Exception("HALT AND CATCH FIRE: operation={}, mode_map={}".format(operation, mode_map))
        return func(self, mode_map)

    def add(self, mode_map: int):
        self.add_to_instruction_history(4)
        a = self.get(1, mode_map)
        b = self.get(2, mode_map)
        self.set(3, a + b, mode_map)
        self.index += 4

    def multiply(self, mode_map: int):
        self.add_to_instruction_history(4)
        a = self.get(1, mode_map)
        b = self.get(2, mode_map)
        self.set(3, a * b, mode_map)
        self.index += 4

    def get_input(self, mode_map: int):
        self.add_to_instruction_history(2)
        if not self.input_buffer:
            raise ValueError("Input buffer is empty")
        input_num = self.input_buffer.pop(0)
        # print("Using input: {}".format(input_num))
        self.set(1, input_num, mode_map)
        self.index += 2

    def send_output(self, mode_map: int):
        self.add_to_instruction_history(2)
        self.diagnostic_code = self.get(1, mode_map)
        self.index += 2

    def jump_if_true(self, mode_map: int):
        self.add_to_instruction_history(3)
        if self.get(1, mode_map):
            self.index = self.get(2, mode_map)
        else:
            self.index += 3

    def jump_if_false(self, mode_map: int):
        self.add_to_instruction_history(3)
        if not self.get(1, mode_map):
            self.index = self.get(2, mode_map)
        else:
            self.index += 3

    def less_than(self, mode_map: int):
        self.add_to_instruction_history(4)
        value = 1 if self.get(1, mode_map) < self.get(2, mode_map) else 0
        self.set(3, value, mode_map)
        self.index += 4

    def equal(self, mode_map: int):
        self.add_to_instruction_history(4)
        value = 1 if self.get(1, mode_map) == self.get(2, mode_map) else 0
        self.set(3, value, mode_map)
        self.index += 4

    operations = {
        1: add,
        2: multiply,
        3: get_input,
        4: send_output,
        5: jump_if_true,
        6: jump_if_false,
        7: less_than,
        8: equal
    }

    def add_to_instruction_history(self, i):
        self.last_instructions.append(self.tape[self.index: self.index + i])

    def get(self, pos: int, mode_map: int) -> int:
        mode = self.get_mode(pos, mode_map)
        if mode == Mode.POSITIONAL.value:
            return self.tape[self.tape[self.index + pos]]
        elif mode == Mode.IMMEDIATE.value:
            return self.tape[self.index + pos]
        else:
            raise Exception("HALT AND CATCH FIRE")

    def set(self, pos: int, value: int, mode_map: int):
        mode = self.get_mode(pos, mode_map)
        if mode == Mode.POSITIONAL.value:
            self.tape[self.tape[self.index + pos]] = value
        elif mode == Mode.IMMEDIATE.value:
            self.tape[self.index + pos] = value
        else:
            raise Exception("HALT AND CATCH FIRE")

    def get_mode(self, pos: int, mode_map: int):
        return (mode_map // (10 ** (pos - 1))) % 10


class DiagnosticCodeError(Exception):
    def __init__(self, code, tape, last_instructions):
        self.code = code
        self.tape = tape
        self.last_instructions = last_instructions


def get_amplified_output(program: str, phase_setting: int, amp_input: int):
    intcode = IntCode(program, [phase_setting, amp_input])
    return intcode.run()


def run_amplifiers(program: str, amp_modes: Union[str, List[int]]):
    if isinstance(amp_modes, str):
        amp_modes = [int(c) for c in amp_modes]
    output = 0
    for m in amp_modes:
        output = IntCode(program, [m, output]).run()
    return output


def in_base(num, base):
    if not isinstance(base, int) or base <= 1:
        return ValueError("Invalid base {}".format(base))
    if num == 0:
        return "0"
    s = ""
    while num > 0:
        s = str(num % base) + s
        num //= base
    return s


def find_max_thruster_setting(program: str):
    max_thrust = 0
    max_mode = 0
    for i in range(MAX_AMP_MODE + 1):
        mode = "{:>05}".format(in_base(i, AMP_MODE_BASE))
        thrust = run_amplifiers(program, mode)
        if thrust > max_thrust:
            max_thrust = thrust
            max_mode = mode
    return max_mode
