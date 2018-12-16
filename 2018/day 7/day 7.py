import re
from typing import List

example = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""


class Node:

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def add_parent(self, node: "Node"):
        self.parents.append(node)

    def add_child(self, node: "Node"):
        self.children.append(node)
        node.add_parent(self)

    def has_parent(self):
        return len(self.parents) > 0

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def __str__(self):
        return (f"Node(name={self.name}, parents={[n.get_name() for n in self.parents]}, " +
                f"children={[n.get_name() for n in self.children]})")

    def __repr__(self):
        return str(self)


reg = r"Step (\w+) must be finished before step (\w+) can begin."


def preprocess_input(in_str):
    return re.findall(reg, in_str)


def sort_nodes(node_list) -> List[Node]:
    return sorted(node_list, key=lambda n: n.get_name())


def find_node_by_name(node_list, name) -> Node:
    for n in node_list:
        if n.get_name() == name:
            return n
    raise ValueError


def get_start_nodes(node_list):
    start_node_list = [n for n in node_list if not n.has_parent()]
    return start_node_list


def pop_node(node_list: List[Node], completed_nodes: List[str]):
    """
    :param node_list: List of nodes ready to be processed
    :param completed_nodes: List of node names that have been completed
    :return:
    """
    sorted_list = sort_nodes(node_list)
    for n in sorted_list:
        parent_names = [_.get_name() for _ in n.parents]
        # If all the node's parents have been completed
        if not set(parent_names).difference(completed_nodes):
            sorted_list.remove(n)
            sorted_list += n.get_children()
            return n, list(set(sorted_list))
    raise ValueError


def prep_node_list(in_str):
    pair_list = preprocess_input(in_str)
    # Flatten lists
    node_names = set([item for sublist in pair_list for item in sublist])
    # Create nodes
    nodes = sort_nodes([Node(name) for name in node_names])
    # Match parents with children
    for parent, child in pair_list:
        parent_node = find_node_by_name(nodes, parent)
        child_node = find_node_by_name(nodes, child)
        parent_node.add_child(child_node)
    return nodes


def find_node_order(node_list: List[Node]):
    # Get starting node
    node_tracker = get_start_nodes(node_list)
    node_order = []
    # Cycle through node tree
    while True:
        popped_node, node_tracker = pop_node(node_tracker, node_order)
        node_order.append(popped_node.get_name())
        if not node_tracker:
            return node_order


def day_7_a(in_str):
    nodes = prep_node_list(in_str)
    print(nodes)
    node_order = find_node_order(nodes)
    print(node_order)
    return "".join(node_order)


assert day_7_a(example) == "CABDFE"
with open("day 7.input") as f:
    print(day_7_a(f.read()))


