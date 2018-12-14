import re

day_5_example = "dabAcCaCBAcCcaDA"

reg = re.compile(r"([a-z])(\1)", re.IGNORECASE)


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
                polymer = polymer.replace(''.join(m), '', 1)
                break
        else:
            return polymer


print(len(collapse_polymer(day_5_example)))
with open("day 5.input") as f:
    print(len(collapse_polymer(f.read())))
