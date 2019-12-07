from typing import List, Tuple


class Orbit:
    name = ""
    children = []

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child: "Orbit"):
        if child in self.children:
            raise KeyError(f"{child.name} already in orbit around {self.name}")
        self.children.append(child)

    def get_children(self) -> List["Orbit"]:
        return self.children

    def get_checksum(self, level):
        checksum = level
        for c in self.get_children():
            checksum += c.get_checksum(level + 1)
        return checksum

    def get_orbit_path(self, orbit_path, name):
        new_orbit_path = orbit_path + [self.name]
        if self.name == name:
            return new_orbit_path
        for c in self.get_children():
            op = c.get_orbit_path(new_orbit_path, name)
            if op:
                return op
        return None


class OrbitCollection:

    orbit_dict = {}

    def __init__(self):
        self.orbit_dict = {"COM": Orbit("COM")}

    def get(self, name: str) -> Orbit:
        if name not in self.orbit_dict:
            self.orbit_dict[name] = Orbit(name)
        return self.orbit_dict[name]

    def add_orbit(self, parent: str, child: str):
        self.get(parent).add_child(self.get(child))

    def get_orbit_checksum(self):
        return self.orbit_dict["COM"].get_checksum(0)

    def get_orbit_path(self, name):
        return self.orbit_dict["COM"].get_orbit_path([], name)


def parse_input(s: str) -> List[List[str]]:
    orbit_list = []
    if s:
        for line in s.strip().split("\n"):
            orbit_list.append(line.strip().split(")"))
    return orbit_list


def add_orbits_to_collection(orbit_list: List[List[str]]) -> OrbitCollection:
    orbit_collection = OrbitCollection()
    for parent, child in orbit_list:
        orbit_collection.add_orbit(parent, child)
    return orbit_collection


def get_checksum(s: str):
    orbit_collection = add_orbits_to_collection(parse_input(s))
    return orbit_collection.get_orbit_checksum()


assert get_checksum("") == 0
assert get_checksum("COM)B") == 1
assert get_checksum("""
COM)B
B)C
""") == 3
assert get_checksum("""
COM)B
B)C
C)D
""") == 6
assert get_checksum("""
COM)B
COM)C
COM)D
""") == 3
assert get_checksum("""
COM)B
B)C
B)D
""") == 5
assert get_checksum("""
B)C
B)D
COM)B
""") == 5
assert get_checksum("""
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
COM)B
J)K
K)L
""") == 42


# with open("input.text") as f:
#     print(get_checksum(f.read()))


def get_orbit_path(s, target):
    orbit_collection = add_orbits_to_collection(parse_input(s))
    return orbit_collection.get_orbit_path(target)


assert get_orbit_path("COM)A", "A") == ["COM", "A"]
practice_orbits = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""
assert get_orbit_path(practice_orbits, "YOU") == ["COM", "B", "C", "D", "E", "J", "K", "YOU"]
assert get_orbit_path(practice_orbits, "SAN") == ["COM", "B", "C", "D", "I", "SAN"]


def get_orbital_transfer_number(s, origin="YOU", target="SAN"):
    orbit_collection = add_orbits_to_collection(parse_input(s))
    you_list = orbit_collection.get_orbit_path(origin)
    san_list = orbit_collection.get_orbit_path(target)
    total_steps = len(you_list) + len(san_list)
    for i in range(len(you_list)):
        # print(you_list[i], san_list[i])
        total_steps -= 2
        if you_list[i] != san_list[i]:
            break
    return total_steps


assert get_orbital_transfer_number(practice_orbits) == 4


with open("input.text") as f:
    print(get_orbital_transfer_number(f.read()))
