import re

day_5_example = "dabAcCaCBAcCcaDA"
day_5_test_1 = "bbAAaBb"
day_5_test_2 = "BbAAaBb"

reg = re.compile(r"(?=([a-z])(\1))", re.IGNORECASE)


def react_polymer(polymer):
    # iters = 0
    while True:
        # iters += 1
        # if iters % 1000 == 0:
        #     print(f"{iters}: {len(polymer)}")
        matches = re.findall(reg, polymer)
        for m in matches:
            if m[0] != m[1]:
                # print(polymer)
                polymer = polymer.replace(''.join(m), '')
                break
        else:
            return polymer


assert len(react_polymer(day_5_example)) == 10
assert len(react_polymer(day_5_test_1)) == 3
assert len(react_polymer(day_5_test_2)) == 1
with open("day 5.input") as f:
    print(len(react_polymer(f.read().strip())))


def find_shortest_polymer(polymer: str):
    polymer_set = sorted(list(set(polymer.lower())))
    polymer_dict = {}
    for p in polymer_set:
        polymer_candidate = polymer.replace(p, '').replace(p.upper(), '')
        reacted_polymer = react_polymer(polymer_candidate)
        print(f"{p} => {len(reacted_polymer)}")
        polymer_dict[p] = len(reacted_polymer)
    return min(polymer_dict.values())


assert find_shortest_polymer(day_5_example) == 4
with open("day 5.input") as f:
    print(find_shortest_polymer(f.read().strip()))
