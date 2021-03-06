import unittest
from contextlib import redirect_stdout
from io import StringIO

from aoc_2019.common.intcode import IntCode, OutOfTapeException, InvalidOperationException, EmptyInputBufferException


class TestIntCode(unittest.TestCase):

    def test_addition(self):
        intcode = IntCode("1,0,0,0,99")
        intcode.run()
        self.assertEqual([2, 0, 0, 0, 99], intcode.get_tape())
        intcode = IntCode("1,2,3,5,99,0")
        intcode.run()
        self.assertEqual([1, 2, 3, 5, 99, 8], intcode.get_tape())

    def test_multiplication(self):
        intcode = IntCode("2,3,0,3,99")
        intcode.run()
        self.assertEqual([2, 3, 0, 6, 99], intcode.get_tape())
        intcode = IntCode("2,4,4,5,99,0")
        intcode.run()
        self.assertEqual([2, 4, 4, 5, 99, 9801], intcode.get_tape())

    def test_mixed(self):
        intcode = IntCode("1,9,10,3,2,3,11,0,99,30,40,50")
        intcode.run()
        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50], intcode.get_tape())

    def test_multiple_halts(self):
        intcode = IntCode("1,1,1,4,99,5,6,0,99")
        intcode.run()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], intcode.get_tape())

    def test_no_halt(self):
        with self.assertRaises(OutOfTapeException):
            IntCode("2,2,3,2").run()

    def test_invalid_operation(self):
        with self.assertRaises(InvalidOperationException):
            IntCode("2,2,3,2,98").run()

    def test_empty_input_buffer(self):
        with self.assertRaises(EmptyInputBufferException):
            IntCode("3,1,99").run()

    def test_immediate_mode(self):
        self.assertEqual(None, IntCode("1002,4,3,4,33").run())
        self.assertEqual(None, IntCode("1101,100,-1,4,0").run())
        self.assertEqual(5, IntCode("104, 5, 99").run())
        intcode = IntCode("103, 1, 4, 1, 99")
        intcode.add_to_input_buffer(5)
        self.assertEqual(5, intcode.run())

    def test_multiple_outputs(self):
        intcode = IntCode("1, 5, 5, 1, 1, 7, 7, 9, 104, 0, 104, 22, 104, 33, 99")
        self.assertEqual(18, intcode.run())
        self.assertFalse(intcode.halted)
        self.assertEqual(22, intcode.run())
        self.assertFalse(intcode.halted)
        self.assertEqual(33, intcode.run())
        self.assertFalse(intcode.halted)
        self.assertIsNone(intcode.run())
        self.assertTrue(intcode.halted)

    def test_equal_positional(self):
        self.assertEqual(1, IntCode("3,9,8,9,10,9,4,9,99,-1,8").add_to_input_buffer(8).run())
        self.assertEqual(0, IntCode("3,9,8,9,10,9,4,9,99,-1,8").add_to_input_buffer(6).run())

    def test_less_than_positional(self):
        self.assertEqual(1, IntCode("3,9,7,9,10,9,4,9,99,-1,8").add_to_input_buffer(3).run())
        self.assertEqual(0, IntCode("3,9,7,9,10,9,4,9,99,-1,8").add_to_input_buffer(10).run())

    def test_equal_immediate(self):
        self.assertEqual(1, IntCode("3,3,1108,-1,8,3,4,3,99").add_to_input_buffer(8).run())
        self.assertEqual(0, IntCode("3,3,1108,-1,8,3,4,3,99").add_to_input_buffer(6).run())

    def test_less_than_immediate(self):
        self.assertEqual(1, IntCode("3,3,1107,-1,8,3,4,3,99").add_to_input_buffer(3).run())
        self.assertEqual(0, IntCode("3,3,1107,-1,8,3,4,3,99").add_to_input_buffer(10).run())

    def test_jump_if_true(self):
        self.assertEqual(None, IntCode("1105,0,4,99,104,1,99").run())
        self.assertEqual(1, IntCode("1105,1,4,99,104,1,99").run())
        self.assertEqual(0, IntCode("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9").add_to_input_buffer(0).run())
        self.assertEqual(1, IntCode("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9").add_to_input_buffer(10).run())

    def test_jump_if_false(self):
        self.assertEqual(1, IntCode("1106,0,4,99,104,1,99").run())
        self.assertEqual(None, IntCode("1106,1,4,99,104,1,99").run())
        self.assertEqual(0, IntCode("3,3,1105,-1,9,1101,0,0,12,4,12,99,1").add_to_input_buffer(0).run())
        self.assertEqual(1, IntCode("3,3,1105,-1,9,1101,0,0,12,4,12,99,1").add_to_input_buffer(10).run())

    def test_example_comparator(self):
        program = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1," \
                  "46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
        self.assertEqual(999, IntCode(program).add_to_input_buffer(7).run())
        self.assertEqual(1000, IntCode(program).add_to_input_buffer(8).run())
        self.assertEqual(1001, IntCode(program).add_to_input_buffer(9).run())

    def test_pretty_print(self):
        f = StringIO()
        with redirect_stdout(f):
            IntCode("1,2,3,5,99,0").pprint()
        expected = [
            "0000 add pos(2) pos(3) pos(5)",
            "0004 hal ",
            "0005 nop ",
        ]
        self.assertEqual("\n".join(expected) + "\n", f.getvalue())

    def test_pretty_print_imm(self):
        f = StringIO()
        with redirect_stdout(f):
            IntCode("1001,2,3,5,99,0").pprint()
        expected = [
            "0000 add pos(2) imm(3) pos(5)",
            "0004 hal ",
            "0005 nop ",
        ]
        self.assertEqual("\n".join(expected) + "\n", f.getvalue())

    def test_pretty_print_all_ops(self):
        f = StringIO()
        with redirect_stdout(f):
            IntCode("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,"
                    "1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99,209,69").pprint()
        expected = [
            "0000 inp pos(21)",
            "0002 equ pos(21) imm(8) pos(20)",
            "0006 jmt pos(20) imm(22)",
            "0009 lth imm(8) pos(21) pos(20)",
            "0013 jmf pos(20) imm(31)",
            "0016 jmf imm(0) imm(36)",
            "0019 nop ",
            "0020 nop ",
            "0021 nop ",
            "0022 mul pos(21) imm(125) pos(20)",
            "0026 out pos(20)",
            "0028 jmt imm(1) imm(46)",
            "0031 out imm(999)",
            "0033 jmt imm(1) imm(46)",
            "0036 add imm(1000) imm(1) pos(20)",
            "0040 out pos(20)",
            "0042 jmt imm(1) imm(46)",
            "0045 nop ",
            "0046 hal ",
            "0047 rel rel(69)"
        ]
        self.assertEqual("\n".join(expected) + "\n", f.getvalue())

    def test_pprint_instruction(self):
        f = StringIO()
        with redirect_stdout(f):
            IntCode("3,21,1008,21,8,20").pprint_instruction(2)
        self.assertEqual("0002 equ pos(21) imm(8) pos(20)\n", f.getvalue())

    def test_pprint_instruction_unroll(self):
        f = StringIO()
        with redirect_stdout(f):
            IntCode("3,21,8,0,1,2").pprint_instruction(2, unroll=True)
        self.assertEqual("0002 equ pos(0 -> 3) pos(1 -> 21) pos(2 -> 8)\n", f.getvalue())

    def test_relative_base(self):
        intcode = IntCode("109,15,204,-6,109,-10,204,5,99,27,28")
        self.assertEqual(0, intcode.relative_base)
        self.assertEqual(27, intcode.run())
        self.assertEqual(15, intcode.relative_base)
        self.assertEqual(28, intcode.run())
        self.assertEqual(5, intcode.relative_base)

    def test_day_9_example_1(self):
        s = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        self.assertEqual(s, IntCode(s).run_until_halted())

    def test_day_9_example_2(self):
        s = "1102,34915192,34915192,7,4,7,99,0"
        self.assertEqual(16, len(str(IntCode(s).run())))

    def test_day_9_example_3(self):
        self.assertEqual(1125899906842624, IntCode("104,1125899906842624,99").run())

    def test_day_9_part_1(self):
        with open("../../day_9/input.text") as f:
            intcode = IntCode(f.read())
        intcode.add_to_input_buffer(1)
        self.assertEqual(2789104029, intcode.run())

    def test_day_9_part_2(self):
        with open("../../day_9/input.text") as f:
            intcode = IntCode(f.read())
        intcode.add_to_input_buffer(2)
        print(intcode.run())


if __name__ == "__main__":
    unittest.main()
