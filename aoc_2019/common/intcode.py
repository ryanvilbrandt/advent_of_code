from enum import Enum
from typing import List


class Mode(Enum):
    POSITIONAL = 0
    IMMEDIATE = 1


class IntCode:

    def __init__(self, tape: str, input_buffer: List[int]=None):
        self.tape = [int(i.strip()) for i in tape.split(',')]
        self.index = 0
        self.last_instructions = []
        self.input_buffer = input_buffer if input_buffer is not None else []
        self.halted = False

    def add_to_input_buffer(self, value):
        self.input_buffer.append(value)
        return self

    def run(self):
        while not self.halted:
            if self.index >= len(self.tape):
                raise OutOfTapeException()
            # self.print_tape()
            output = self.instruction()
            if output is not None:
                return output

    def print_tape(self):
        print(self.tape)
        indent = len(", ".join([str(i) for i in self.tape[:self.index + 1]]))
        print(indent * " " + "^")

    def instruction(self):
        operation, mode_map = self.tape[self.index] % 100, self.tape[self.index] // 100
        func = self.operations.get(operation)
        if func is None:
            raise InvalidOperationException("operation={}, mode_map={}".format(operation, mode_map))
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
            raise EmptyInputBufferException()
        input_num = self.input_buffer.pop(0)
        # print("Using input: {}".format(input_num))
        self.set(1, input_num, mode_map)
        self.index += 2

    def send_output(self, mode_map: int):
        self.add_to_instruction_history(2)
        diagnostic_code = self.get(1, mode_map)
        self.index += 2
        return diagnostic_code

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

    def halt(self, mode_map: int):
        self.add_to_instruction_history(1)
        self.halted = True

    operations = {
        1: add,
        2: multiply,
        3: get_input,
        4: send_output,
        5: jump_if_true,
        6: jump_if_false,
        7: less_than,
        8: equal,
        99: halt
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

    @staticmethod
    def get_mode(pos: int, mode_map: int):
        return (mode_map // (10 ** (pos - 1))) % 10

    def __str__(self):
        return f"IntCode()"

    def __repr__(self):
        return f"IntCode(index={self.index}, input_buffer={self.input_buffer})"

    def pprint(self):
        index = 0
        while index < len(self.tape):
            op_code = self.tape[index]
            mode_op = op_code % 100
            mode_params = op_code // 100
            if mode_op == 1:
                op = "add"
                num_params = 3
            elif mode_op == 2:
                op = "mul"
                num_params = 3
            elif mode_op == 3:
                op = "inp"
                num_params = 1
            elif mode_op == 4:
                op = "out"
                num_params = 1
            elif mode_op == 5:
                op = "jmt"
                num_params = 2
            elif mode_op == 6:
                op = "jmf"
                num_params = 2
            elif mode_op == 7:
                op = "lth"
                num_params = 3
            elif mode_op == 8:
                op = "equ"
                num_params = 3
            elif mode_op == 99:
                op = "hal"
                num_params = 0
            else:
                op = "nop"
                num_params = 0
            params = []
            for i in range(num_params):
                param_mode = "pos" if mode_params % 10 == 0 else "imm"
                mode_params //= 10
                params.append("{}({})".format(param_mode, self.tape[index + i + 1]))
            print("{:>04} {} {}".format(index, op, " ".join(params)))
            index += 1 + num_params


class OutOfTapeException(Exception):
    pass


class InvalidOperationException(Exception):
    pass


class EmptyInputBufferException(Exception):
    pass
