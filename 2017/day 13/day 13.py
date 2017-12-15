from typing import Dict, List


def build_firewall(text):
    text = text.strip('\n').split('\n')
    firewall_dict = {}
    for line in text:
        level, sc_range = line.split(': ')
        firewall_dict[int(level)] = [0, int(sc_range), 1]
    print(firewall_dict)
    return firewall_dict


def advance_scanners(firewall: Dict[int, List[int]]):
    for k in firewall:
        sc_position, sc_range, sc_direction = firewall[k]
        if ((sc_direction == 1 and sc_position == sc_range - 1) or
            (sc_direction == -1 and sc_position == 0)):
            sc_direction *= -1
            firewall[k][2] = sc_direction
        sc_position += sc_direction
        firewall[k][0] = sc_position
    # print(firewall)
    return firewall

def walk_firewall(firewall: Dict[int, List[int]], delay=0, break_on_caught=False):
    if delay > 0:
        for i in range(delay):
            firewall = advance_scanners(firewall)

    max_level = max(list(firewall.keys()))
    severity = 0
    for i in range(max_level + 1):
        level = firewall.get(i)
        if level and level[0] == 0:
            severity += (i * level[1])
            print(i, "--", firewall)
            if break_on_caught:
                return False
        firewall = advance_scanners(firewall)
    return severity

def find_safe_path(firewall: Dict[int, List[int]], max_delay=11):
    for i in range(max_delay):
        print(">", i)
        severity = walk_firewall(firewall, delay=i, break_on_caught=True)
        if severity is not False:
            return i


a = """
0: 3
1: 2
4: 4
6: 4
"""
# with open("day 13.input") as f:
#     a = f.read()

# print(walk_firewall(build_firewall(a)))
print(find_safe_path(build_firewall(a)))
