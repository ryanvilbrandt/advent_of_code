import re


class Village:

    name = None
    links = None

    def __init__(self, name: int):
        self.name = name
        self.links = []

    def add_link(self, new_link: "Village"):
        if new_link not in self.links:
            self.links.append(new_link)
            new_link.add_link(self)

    def find_group(self, group=None):
        if group is None:
            group = []
        if self.name in group:
            return
        group.append(self.name)
        for link in self.links:
            link.find_group(group)
        return group

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return "Village(name={}, links={})".format(self.name, [link.name for link in self.links])


def build_graph(text: str):
    graph_dict = {}

    villages_text = text.strip("\n").split("\n")
    reg = re.compile(r"(\d+) <-> ([\d, ]+)")

    # Build initial villages
    for line in villages_text:
        m = re.match(reg, line)
        graph_dict[int(m.group(1))] = Village(int(m.group(1)))

    # Link villages
    for line in villages_text:
        m = re.match(reg, line)
        for link in m.group(2).split(", "):
            graph_dict[int(m.group(1))].add_link(graph_dict[int(link)])

    return graph_dict

def find_all_groups(text: str):
    graph_dict = build_graph(text)

    program_names = list(graph_dict.keys())
    total_groups = []

    while program_names:
        group = graph_dict[program_names[0]].find_group()
        total_groups.append(group)
        program_names = list(set(program_names) - set(group))
    return total_groups


a = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""
print(len(find_all_groups(a)))

with open("day 12.input") as f:
    a = f.read()

print(len(find_all_groups(a)))


