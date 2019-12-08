import unittest

from .problem import get_amplified_output, run_amplifiers, find_max_thrust

A_PLUS_B = "3,11,3,12,1,11,12,13,4,13,99,0,0,0"


class TestDay7(unittest.TestCase):

    def test_get_amplified_output(self):
        self.assertEqual(7, get_amplified_output(A_PLUS_B, 5, 2))
        self.assertEqual(12, get_amplified_output(A_PLUS_B, 8, 4))

    def test_run_amplifiers(self):
        self.assertEqual(1, run_amplifiers(A_PLUS_B, "1"))
        self.assertEqual(3, run_amplifiers(A_PLUS_B, "12"))
        self.assertEqual(15, run_amplifiers(A_PLUS_B, "12345"))
    
    def test_find_max_thrust(self):
        self.assertEqual(10, find_max_thrust(A_PLUS_B))

    def test_example_program_1(self):
        s = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
        self.assertEqual(43210, run_amplifiers(s, "43210"))
        self.assertEqual(43210, find_max_thrust(s))

    def test_example_program_2(self):
        s = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
        self.assertEqual(54321, run_amplifiers(s, "01234"))
        self.assertEqual(54321, find_max_thrust(s))

    def test_example_program_3(self):
        s = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        self.assertEqual(65210, run_amplifiers(s, "10432"))
        self.assertEqual(65210, find_max_thrust(s))

    def test_part_1(self):
        with open("day_7/input.text") as f:
            self.assertEqual(14902, find_max_thrust(f.read()))

    def test_example_program_4(self):
        s = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
        self.assertEqual(139629729, run_amplifiers(s, "98765"))
        self.assertEqual(139629729, find_max_thrust(s, [5, 6, 7, 8, 9]))

    def test_example_program_5(self):
        s = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53," \
            "1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
        self.assertEqual(18216, run_amplifiers(s, "97856"))
        self.assertEqual(18216, find_max_thrust(s, [5, 6, 7, 8, 9]))

    def test_part_2(self):
        with open("day_7/input.text") as f:
            self.assertEqual(6489132, find_max_thrust(f.read(), [5, 6, 7, 8, 9]))


if __name__ == "__main__":
    unittest.main()
