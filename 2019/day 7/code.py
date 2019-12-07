import time


class IntCode:

    def __init__(self, tape: str, test_input=None):
        self.tape = [int(i.strip()) for i in tape.split(',')]
        self.index = 0
        self.diagnostic_code = 0
        self.last_instructions = []
        self.test_input = test_input

    def run(self):
        self.index = 0
        while True:
            # print(self.tape)
            # print(self.index)
            if self.tape[self.index] == 99:
                return self.tape, self.diagnostic_code
            if self.diagnostic_code != 0:
                raise DiagnosticCodeError(
                    self.diagnostic_code,
                    self.tape,
                    self.last_instructions
                )
            self.instruction()
            # time.sleep(1)

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
        if self.test_input is not None:
            input_num = self.test_input
        else:
            while True:
                s = input("Gimme a number, dawg: ")
                if not s.isnumeric():
                    print("That's not a number, dawg.")
                else:
                    input_num = int(s)
                    break
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
        if mode == 0:
            return self.tape[self.tape[self.index + pos]]
        elif mode == 1:
            return self.tape[self.index + pos]
        else:
            raise Exception("HALT AND CATCH FIRE")

    def set(self, pos: int, value: int, mode_map: int):
        mode = self.get_mode(pos, mode_map)
        if mode == 0:
            self.tape[self.tape[self.index + pos]] = value
        elif mode == 1:
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


def assert_intcode(intcode_in: str, expected_intcode: str=None, code=None, test_input=None):
    tape, diagnostic_code = IntCode(intcode_in, test_input=test_input).run()
    if expected_intcode is not None:
        intcode_results = ",".join([str(c) for c in tape])
        assert intcode_results == expected_intcode
    if code is not None:
        if not diagnostic_code == code:
            print(tape)
            raise AssertionError(
                "diagnostic_code ({}) does not match expected code ({})".format(
                    diagnostic_code, code
                )
            )


assert_intcode("1002,4,3,4,33", "1002,4,3,4,99", 0)
assert_intcode("1101,100,-1,4,0", "1101,100,-1,4,99", 0)
assert_intcode("104,5,99", "104,5,99", 5)
assert_intcode("103, 1, 4, 1, 99", code=5, test_input=5)
try:
    IntCode("1, 5, 5, 1, 1, 7, 7, 9, 104, 0, 104, 0, 104, 0, 104, 0, 104, 0, 99").run()
except DiagnosticCodeError as e:
    assert e.code == 18
    assert e.tape == [1, 14, 5, 1, 1, 7, 7, 9, 104, 18, 104, 0, 104, 0, 104, 0, 104, 0, 99]
    assert e.last_instructions[-2] == [1, 7, 7, 9]
assert_intcode("3,9,8,9,10,9,4,9,99,-1,8", code=1, test_input=8)
assert_intcode("3,9,8,9,10,9,4,9,99,-1,8", code=0, test_input=6)
assert_intcode("3,9,7,9,10,9,4,9,99,-1,8", code=1, test_input=3)
assert_intcode("3,9,7,9,10,9,4,9,99,-1,8", code=0, test_input=10)
assert_intcode("3,3,1108,-1,8,3,4,3,99", code=1, test_input=8)
assert_intcode("3,3,1108,-1,8,3,4,3,99", code=0, test_input=6)
assert_intcode("3,3,1107,-1,8,3,4,3,99", code=1, test_input=3)
assert_intcode("3,3,1107,-1,8,3,4,3,99", code=0, test_input=10)
assert_intcode("1105,0,4,99,104,1,99", code=0)
assert_intcode("1105,1,4,99,104,1,99", code=1)
assert_intcode("1106,0,4,99,104,1,99", code=1)
assert_intcode("1106,1,4,99,104,1,99", code=0)
assert_intcode("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", code=0, test_input=0)
assert_intcode("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", code=1, test_input=10)
assert_intcode("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", code=0, test_input=0)
assert_intcode("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", code=1, test_input=10)
input_str = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
try:
    assert_intcode(input_str, test_input=7)
except DiagnosticCodeError as e:
    assert e.code == 999
try:
    assert_intcode(input_str, test_input=8)
except DiagnosticCodeError as e:
    assert e.code == 1000
try:
    assert_intcode(input_str, test_input=9)
except DiagnosticCodeError as e:
    assert e.code == 1001

with open("input.text") as f:
    tape, diagnotic_code = IntCode(f.read()).run()
    print(diagnotic_code)
