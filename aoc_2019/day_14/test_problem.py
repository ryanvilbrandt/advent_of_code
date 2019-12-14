import unittest

from aoc_2019.day_14.problem import *


class TestDay14(unittest.TestCase):

    def test_Reaction_from_string(self):
        reaction = Reaction.from_string("7 A, 1 E => 1 FUEL")
        print(reaction)

    def test_ReactionTree_from_string(self):
        s = """
            10 ORE => 10 A
            1 ORE => 1 B
            7 A, 1 B => 1 C
            7 A, 1 C => 1 D
            7 A, 1 D => 1 E
            7 A, 1 E => 1 FUEL
        """
        reaction_tree = ReactionTree.from_string(s)
        reaction_tree.print_reactions()

    def test_get_ore_count_per_fuel_1(self):
        self.assertEqual(1, ReactionTree.from_string("1 ORE => 1 FUEL").get_ore_count_per_fuel())
        self.assertEqual(3, ReactionTree.from_string("3 ORE => 1 FUEL").get_ore_count_per_fuel())

    def test_get_ore_count_per_fuel_2(self):
        s = """
            3 ORE => 1 A
            2 A => 1 B
            1 B => 1 FUEL
        """
        self.assertEqual(6, ReactionTree.from_string(s).get_ore_count_per_fuel())

    def test_get_ore_count_per_fuel_multiple_products(self):
        s = """
            4 ORE => 2 FUEL
        """
        self.assertEqual(2, ReactionTree.from_string(s).get_ore_count_per_fuel())
        s = """
            4 ORE => 2 A
            2 A => 1 FUEL
        """
        self.assertEqual(4, ReactionTree.from_string(s).get_ore_count_per_fuel())
        s = """
            4 ORE => 2 A
            3 A => 1 FUEL
        """
        self.assertEqual(8, ReactionTree.from_string(s).get_ore_count_per_fuel())


if __name__ == "__main__":
    unittest.main()
