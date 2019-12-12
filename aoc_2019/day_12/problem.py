from functools import reduce
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

    def get_hash(self):
        return (self.position[0], self.velocity[0]), \
               (self.position[1], self.velocity[1]), \
               (self.position[2], self.velocity[2])


class MoonSystem:

    def __init__(self, moons: List[Moon]):
        self.moons = moons
        self.initial_x, self.initial_y, self.initial_z = self.get_hash()
        self.loops_x,self.loops_y, self.loops_z = None, None, None

    def apply_gravities(self):
        for m in self.moons:
            for n in self.moons:
                if m == n:
                    continue
                m.apply_gravity(n)

    def apply_velocities(self):
        for m in self.moons:
            m.apply_velocity()

    def time_step(self, loops=0):
        self.apply_gravities()
        self.apply_velocities()
        self.check_history(loops)

    def total_energy(self):
        return sum([m.get_energy() for m in self.moons])

    def __str__(self):
        return "MoonSystem({})".format(self.moons)

    @staticmethod
    def from_string(system_string):
        return MoonSystem([Moon.from_string(s.strip()) for s in system_string.strip().split("\n")])

    def get_hash(self):
        x_hash = tuple()
        y_hash = tuple()
        z_hash = tuple()
        for m in self.moons:
            x, y, z = m.get_hash()
            x_hash += x
            y_hash += y
            z_hash += z
        return x_hash, y_hash, z_hash

    def check_history(self, loops):
        """
        Returns True if it detects a loop
        :return:
        """
        x, y, z = self.get_hash()
        if x == self.initial_x and not self.loops_x:
            self.loops_x = loops + 1
        if y == self.initial_y and not self.loops_y:
            self.loops_y = loops + 1
        if z == self.initial_z and not self.loops_z:
            self.loops_z = loops + 1
        if self.loops_x and self.loops_y and self.loops_z:
            raise ValueError

    def find_loop(self, max_iters):
        i = 0
        try:
            for i in range(max_iters):
                self.time_step(i)
        except ValueError as e:
            return self.loops_x, self.loops_y, self.loops_z


def find_factors(n) -> List[List[int]]:
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            if i == 2:
                i += 1
            else:
                i += 2
    return factors


def find_lcm(nums):
    factors_list = [find_factors(n) for n in nums]
    factor_set = set()
    for m in factors_list:
        for n in m:
            factor_set.add(n)
    lcm = 1
    for f in factor_set:
        lcm *= f ** max([factors.count(f) for factors in factors_list])
    return lcm
