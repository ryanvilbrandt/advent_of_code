import re
from typing import Dict, List

from aoc_2020.common import text_to_list


class BagRule:

    def __init__(self, color: str):
        self.color = color
        self.rules = {}
        self.parents = []

    def get_rules(self) -> Dict["BagRule", int]:
        return self.rules

    def get_parents(self) -> List["BagRule"]:
        return self.parents

    def add_parent(self, bag_rule):
        return self.parents.append(bag_rule)

    def add_rules(self, rules: Dict["BagRule", int]):
        self.rules = rules
        for bag_rule in rules.keys():
            bag_rule.add_parent(self)

    def __str__(self):
        return f"BagColor({self.color})"

    def __repr__(self):
        return self.get_tree()

    def get_tree(self):
        if self.rules is None:
            return f"BagColor(color={self.color})"
        return f"BagColor(color={self.color}, rules={self.rules})"

    def short_name(self):
        if self.rules is None:
            return f"BagColor(color={self.color})"
        return f"BagColor(color={self.color}, rules={dict((str(k), v) for k, v in self.get_rules().items())})"

    @staticmethod
    def create_bag_rules(rules_text: str) -> Dict[str, "BagRule"]:
        color_name_to_bag_rule_dict = {}
        text_rules_dict = {}
        # First, create all BagRules and make mapping of color name to BagRule
        for line in text_to_list(rules_text):
            m = re.match(r"^(.*) bags contain (.*)\.$", line)
            bag_rule = BagRule(m.group(1))
            color_name_to_bag_rule_dict[m.group(1)] = bag_rule
            text_rules_dict[bag_rule] = m.group(2)
        # Now assign rules to BagRules objects using other BagRule objects
        for bag_rule, text_rules in text_rules_dict.items():
            if text_rules == "no other bags":
                continue
            rules_dict = {}
            for text_rule in text_rules.split(", "):
                m = re.match(r"(\d+) (.+) bags?", text_rule)
                rules_dict[color_name_to_bag_rule_dict[m.group(2)]] = int(m.group(1))
            bag_rule.add_rules(rules_dict)
        return color_name_to_bag_rule_dict

    def find_all_parents(self):
        parents_found = set()
        for parent in self.get_parents():
            parents_found.add(parent)
            parents_found.update(parent.find_all_parents())
        return parents_found

    def count_child_bags(self) -> int:
        child_count = 0
        for bag_rule, num in self.get_rules().items():
            child_count += num * bag_rule.count_child_bags()
        return child_count + 1


def find_all_parents(rules_text, bag_color):
    bag_rules = BagRule.create_bag_rules(rules_text)
    parents_set = bag_rules[bag_color].find_all_parents()
    return len(parents_set)


def count_child_bags(rules_text, bag_color):
    bag_rules = BagRule.create_bag_rules(rules_text)
    child_count = bag_rules[bag_color].count_child_bags()
    return child_count - 1
