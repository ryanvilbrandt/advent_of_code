import re
from typing import List

day_7_example = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


class Tower:
    name = None
    weight = None
    children = None
    parent = None

    def __init__(self, name: str, weight: int, children: list=None, parent: "Tower"=None):
        self.name = name
        self.weight = weight
        self.children = [] if children is None else children
        if parent is not None:
            self.parent = parent

    def add_child(self, child: "Tower"):
        self.children.append(child)
        child.parent = self

    def get_children(self) -> List["Tower"]:
        return self.children

    def get_root(self) -> "Tower":
        if self.parent is None:
            return self
        return self.parent.get_root()

    def find_unbalanced_tower(self) -> int:
        """
        :return: True if the solution has been found and printed to console.
        """
        if not self.children:
            return self.weight
        child_weights = {}
        for child in self.get_children():
            child_weights[child.name] = child.find_unbalanced_tower()
        if len(set(child_weights.values())) > 1:
            print(self.name)
            print(child_weights)
            print(self.get_children())
            raise Exception
        return self.weight + sum(child_weights.values())

    def print_tower(self, level=0) -> str:
        out_str = level * "    "
        if not self.get_children():
            out_str += "Tower(name={}, weight={})".format(self.name, self.weight)
        else:
            out_str += "Tower(name={}, weight={}, children=[".format(self.name, self.weight)
            for child in self.get_children():
                out_str += "\n" + child.print_tower(level + 1)
            out_str += "\n" + level * "    " + "])"
        return out_str

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return "Tower(name={}, weight={}, children={})".format(self.name, self.weight,
                                                               [child.name for child in self.children])


def build_tower(tower_text) -> Tower:
    tower_dict = {}

    tower_text = tower_text.strip('\n').split('\n')

    # We must create all tower objects before we can assign children
    for line in tower_text:
        m = re.search(r"([a-z]+) \((\d+)\)", line)
        tower_dict[m.group(1)] = Tower(m.group(1), int(m.group(2)))

    # Now assign all children to tower objects that have children
    for line in tower_text:
        m = re.search(r"([a-z]+) \((\d+)\) -> ([a-z ,]+)", line)
        if m:
            root = tower_dict[m.group(1)]
            children = m.group(3).split(', ')
            for child_name in children:
                root.add_child(tower_dict[child_name])

    key, value = tower_dict.popitem()
    tower_root = value.get_root()

    return tower_root


print(build_tower(day_7_example).print_tower())
print()
with open("day 7.input") as f:
    root = build_tower(f.read())

print(root)
print()
try:
    root.find_unbalanced_tower()
except Exception:
    pass