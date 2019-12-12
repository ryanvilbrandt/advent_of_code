from re import match
from typing import List


class Position(list):

    def __init__(self, x, y, z):
        super().__init__()
        self.extend([x, y, z])

    def __repr__(self):
        return "Position({}, {}, {})".format(*self)


class Velocity(list):

    def __init__(self, x=0, y=0, z=0):
        super().__init__()
        self.extend([x, y, z])

    def __repr__(self):
        return "Velocity({}, {}, {})".format(*self)


class Moon:

    def __init__(self, position: Position, velocity: Velocity):
        self.position = position
        self.velocity = velocity

    def cmp(self, a: int, b: int) -> int:
        if a == b:
            return 0
        if a < b:
            return 1
        return -1

    def apply_gravity(self, other_moon: "Moon"):
        for i, pos in enumerate(self.position):
            self.velocity[i] += self.cmp(pos, other_moon.position[i])

    def apply_velocity(self):
        for i, vel in enumerate(self.velocity):
            self.position[i] += vel

    def get_energy(self):
        potential_energy = [abs(n) for n in self.position]
        kinetic_energy = [abs(n) for n in self.velocity]
        return sum(potential_energy) * sum(kinetic_energy)

    def __repr__(self):
        return "Moon({}, {})".format(self.position, self.velocity)

    @staticmethod
    def from_string(s):
        m = match(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", s)
        if not m:
            raise ValueError("Invalid position string: {}".format(s))
        return Moon(Position(int(m.group(1)), int(m.group(2)), int(m.group(3))), Velocity())


class MoonSystem:

    def __init__(self, moons: List[Moon]):
        self.moons = moons

    def apply_gravities(self):
        for m in self.moons:
            for n in self.moons:
                if m == n:
                    continue
                m.apply_gravity(n)

    def apply_velocities(self):
        for m in self.moons:
            m.apply_velocity()

    def time_step(self):
        self.apply_gravities()
        self.apply_velocities()

    def total_energy(self):
        return sum([m.get_energy() for m in self.moons])

    def __str__(self):
        return "MoonSystem({})".format(self.moons)

    @staticmethod
    def from_string(system_string):
        return MoonSystem([Moon.from_string(s.strip()) for s in system_string.strip().split("\n")])
