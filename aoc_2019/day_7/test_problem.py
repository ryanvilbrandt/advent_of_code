import unittest

from .problem import get_amplified_output, run_amplifiers, in_base, AMP_MODE_BASE, MAX_AMP_MODE, \
    find_max_thruster_setting

A_PLUS_B = "3,11,3,12,1,11,12,13,4,13,99,0,0,0"


class TestDay7(unittest.TestCase):

    def test_get_amplified_output(self):
        self.assertEqual(7, get_amplified_output(A_PLUS_B, 5, 2))
        self.assertEqual(12, get_amplified_output(A_PLUS_B, 8, 4))

    def test_run_amplifiers(self):
        self.assertEqual(1, run_amplifiers(A_PLUS_B, "1"))
        self.assertEqual(3, run_amplifiers(A_PLUS_B, "12"))
        self.assertEqual(15, run_amplifiers(A_PLUS_B, "12345"))
    
    def test_in_base(self):
        self.assertEqual("12345", in_base(12345, 10))
        self.assertEqual("1111", in_base(15, 2))
        self.assertEqual("0", in_base(0, AMP_MODE_BASE))
        self.assertEqual("10", in_base(5, AMP_MODE_BASE))
        self.assertEqual("44444", in_base(MAX_AMP_MODE, AMP_MODE_BASE))
        self.assertEqual("00010", "{:>05}".format(in_base(5, AMP_MODE_BASE)))
    
    def test_find_max_thruster_setting(self):
        self.assertEqual("44444", find_max_thruster_setting(A_PLUS_B))

    def test_example_program_1(self):
        self.assertEqual("43210", find_max_thruster_setting("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"))


if __name__ == "__main__":
    unittest.main()
