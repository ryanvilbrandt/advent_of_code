import unittest

from .problem import get_amplified_output, run_amplifiers, find_max_thruster_setting

A_PLUS_B = "3,11,3,12,1,11,12,13,4,13,99,0,0,0"


class TestDay7(unittest.TestCase):

    def test_get_amplified_output(self):
        self.assertEqual(7, get_amplified_output(A_PLUS_B, 5, 2))
        self.assertEqual(12, get_amplified_output(A_PLUS_B, 8, 4))

    def test_run_amplifiers(self):
        self.assertEqual(1, run_amplifiers(A_PLUS_B, "1"))
        self.assertEqual(3, run_amplifiers(A_PLUS_B, "12"))
        self.assertEqual(15, run_amplifiers(A_PLUS_B, "12345"))
    
    def test_find_max_thruster_setting(self):
        self.assertEqual(10, find_max_thruster_setting(A_PLUS_B))

    def test_example_program_1(self):
        self.assertEqual(43210, find_max_thruster_setting("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"))

    def test_example_program_2(self):
        self.assertEqual(54321, find_max_thruster_setting(
            "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
        ))

    def test_example_program_3(self):
        self.assertEqual(65210, find_max_thruster_setting(
            "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        ))

    def test_part_1(self):
        with open("day_7/input.text") as f:
            self.assertEqual(14902, find_max_thruster_setting(f.read()))


if __name__ == "__main__":
    unittest.main()
