import re
from math import ceil
from typing import Dict


class Reaction:

    product = None
    amount = None
    ingredients = None

    def __init__(self, product: str, amount: int, ingredients: Dict[str, int]):
        self.product = product
        self.amount = amount
        self.ingredients = ingredients

    def get_ingredients(self) -> Dict[str, int]:
        return self.ingredients

    @staticmethod
    def from_string(s: str):
        """
        7 A, 1 E => 1 FUEL
        Reaction(FUEL, 1, {'A': 7, 'E': 1})
        """
        m = re.match(r"(.+?) => (\d+) ([A-Z]+)", s)
        ingredients_str, amount, product = m.group(1), int(m.group(2)), m.group(3)
        ingredients = {}
        for ing in re.findall(r"(\d+) ([A-Z]+)", ingredients_str):
            ingredients[ing[1]] = int(ing[0])
        return Reaction(product, amount, ingredients)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"Reaction({self.product}, {self.amount}, {self.ingredients})"


class ReactionTree:

    reactions = None

    def __init__(self):
        self.reactions = {}

    def add_reaction(self, reaction: Reaction):
        self.reactions[reaction.product] = reaction

    @staticmethod
    def from_string(s: str):
        rt = ReactionTree()
        for line in s.strip().split("\n"):
            rt.add_reaction(Reaction.from_string(line.strip()))
        return rt

    def print_reactions(self):
        for r in self.reactions.values():
            print(r)

    def get_reaction(self, name: str) -> Reaction:
        return self.reactions[name]

    def get_ore_count_per_fuel(self):
        return self.get_ore_count("FUEL")

    def get_ore_count(self, name: str):
        if name == "ORE":
            return 1
        node = self.get_reaction(name)
        total_ore_count = 0
        for ing, ing_amount in node.get_ingredients().items():
            total_ore_count += ceil((ing_amount * self.get_ore_count(ing)) / node.amount)
        return total_ore_count
