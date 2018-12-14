import re

day_5_example = "dabAcCaCBAcCcaDA"
day_5_test_1 = "bbAAaBb"
day_5_test_2 = "BbAAaBb"

reg = re.compile(r"(?=([a-z])(\1))", re.IGNORECASE)


def collapse_polymer(polymer):
    iters = 0
    while True:
        iters += 1
        if iters % 1000 == 0:
            print(f"{iters}: {len(polymer)}")
        matches = re.findall(reg, polymer)
        for m in matches:
            if m[0] != m[1]:
                # print(polymer)
                polymer = polymer.replace(''.join(m), '')
                break
        else:
            return polymer


assert len(collapse_polymer(day_5_example)) == 10
assert len(collapse_polymer(day_5_test_1)) == 3
assert len(collapse_polymer(day_5_test_2)) == 1
with open("day 5.input") as f:
    print(len(collapse_polymer(f.read().strip())))
