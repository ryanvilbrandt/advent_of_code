def fuel_needed(module_mass):
    return int(int(module_mass) / 3) - 2


assert fuel_needed(12) == 2
assert fuel_needed(14) == 2
assert fuel_needed(1969) == 654
assert fuel_needed(100756) == 33583

# with open("day 1 a.input") as f:
#     print(sum(map(fuel_needed, f.readlines())))


def fuel_needed_b(module_mass):
    last_mass = module_mass
    total_fuel_mass = 0
    while True:
        more_fuel = int(int(last_mass) / 3) - 2
        if more_fuel <= 0:
            break
        last_mass = more_fuel
        total_fuel_mass += more_fuel
    return total_fuel_mass


assert fuel_needed_b(14) == 2
assert fuel_needed_b(1969) == 966
assert fuel_needed_b(100756) == 50346

with open("day 1 a.input") as f:
    print(sum(map(fuel_needed_b, f.readlines())))
