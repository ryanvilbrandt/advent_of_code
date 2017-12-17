def build_firewall(text):
    text = text.strip('\n').split('\n')
    firewall_dict = {}
    for line in text:
        level, sc_range = line.split(': ')
        firewall_dict[int(level)] = int(sc_range)
    return firewall_dict


def is_caught(steps, sc_range):
    return steps % ((sc_range - 1) * 2) == 0


def walk_firewall(firewall, delay=0, break_on_caught=False):
    max_level = max(list(firewall.keys()))
    severity = 0
    for i in range(max_level + 1):
        sc_range = firewall.get(i)
        if sc_range and is_caught(i + delay, sc_range):
            severity += (i * sc_range)
            if break_on_caught:
                return False
    return severity


def find_safe_path(text, max_delay=1e7):
    max_delay = int(max_delay)
    firewall = build_firewall(text)

    for i in range(max_delay):
        if i % 1e5 == 0:
            print(f"{i} / {max_delay}")
        severity = walk_firewall(firewall, i, break_on_caught=True)
        if severity is not False:
            return i


# a = """
# 0: 3
# 1: 2
# 4: 4
# 6: 4
# """
with open("day 13.input") as f:
    a = f.read()

# print(walk_firewall(build_firewall(a)))
print(find_safe_path(a))
