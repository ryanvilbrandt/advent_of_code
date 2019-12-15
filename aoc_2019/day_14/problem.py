import re
from collections import defaultdict
from math import ceil
from typing import Dict


class Reaction:

    product = None
    produced_amount = None
    ingredients = None

    def __init__(self, product: str, amount: int, ingredients: Dict[str, int]):
        self.product = product
        self.produced_amount = amount
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
        return f"Reaction({self.product!r}, {self.produced_amount!r}, {self.ingredients})"


class ReactionTree:

    reactions = None
    inventory = None
    ore_used = None

    def __init__(self):
        self.reactions = {}
        self.inventory = defaultdict(int)
        self.ore_used = 0

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

    def get_ore_count_per_fuel(self, fuel_amount=1):
        self.inventory = defaultdict(int)
        self.ore_used = 0
        self.make_item("FUEL", fuel_amount)
        return self.ore_used

    def make_item(self, name: str, requested_amount: int):
        if name == "ORE":
            self.ore_used += requested_amount
            return
        if requested_amount > self.inventory[name]:
            node = self.get_reaction(name)
            quantity = int(ceil((requested_amount - self.inventory[name]) / node.produced_amount))
            for ing, ing_amount in node.get_ingredients().items():
                self.make_item(ing, ing_amount * quantity)
            self.inventory[name] += node.produced_amount * quantity
        self.inventory[name] -= requested_amount
        assert self.inventory[name] >= 0

    def find_fuel_output(self, ore_provided: int, fuel_amount_to_check=1):
        last_fuel_amount = fuel_amount_to_check
        while True:
            ore_count = self.get_ore_count_per_fuel(fuel_amount_to_check)
            print("Ore count:", ore_count)
            error_ratio = ore_provided / ore_count
            print("Error ratio:", error_ratio)
            fuel_amount_to_check = int(error_ratio * fuel_amount_to_check)
            print("Fuel amount to check:", fuel_amount_to_check)
            if last_fuel_amount == fuel_amount_to_check:
                break
            last_fuel_amount = fuel_amount_to_check

        return fuel_amount_to_check

