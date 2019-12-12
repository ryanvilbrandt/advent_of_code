import unittest

from aoc_2019.day_12.problem import *


class TestDay10(unittest.TestCase):

    def test_apply_gravity(self):
        moon1 = Moon(Position(1, 1, 1), Velocity())
        moon2 = Moon(Position(2, 2, 2), Velocity())
        moon1.apply_gravity(moon2)
        self.assertEqual(Velocity(1, 1, 1), moon1.velocity)
        moon2.position = Position(-5, 1, 5)
        moon1.apply_gravity(moon2)
        self.assertEqual(Velocity(0, 1, 2), moon1.velocity)

    def test_apply_velocity(self):
        europa = Moon(Position(1, 2, 3), Velocity(-2, 0, 3))
        europa.apply_velocity()
        self.assertEqual(Position(-1, 2, 6), europa.position)

    def test_apply_gravity_to_system_1(self):
        moon1 = Moon(Position(1, 1, 1), Velocity())
        moon2 = Moon(Position(2, 2, 2), Velocity())
        moon3 = Moon(Position(3, 3, 3), Velocity())
        system = MoonSystem([moon1, moon2, moon3])
        system.apply_gravities()
        self.assertEqual(Velocity(2, 2, 2), moon1.velocity)
        self.assertEqual(Velocity(0, 0, 0), moon2.velocity)
        self.assertEqual(Velocity(-2, -2, -2), moon3.velocity)

    def test_apply_gravity_to_system_2(self):
        moon1 = Moon(Position(1, 2, 3), Velocity())
        moon2 = Moon(Position(2, 2, 5), Velocity())
        moon3 = Moon(Position(6, 2, 3), Velocity())
        system = MoonSystem([moon1, moon2, moon3])
        system.apply_gravities()
        self.assertEqual(Velocity(2, 0, 1), moon1.velocity)
        self.assertEqual(Velocity(0, 0, -2), moon2.velocity)
        self.assertEqual(Velocity(-2, 0, 1), moon3.velocity)

    def test_apply_velocity_to_system(self):
        moon1 = Moon(Position(1, 1, 1), Velocity(1, 2, 3))
        moon2 = Moon(Position(2, 2, 2), Velocity(3, 2, 1))
        moon3 = Moon(Position(3, 3, 3), Velocity(-2, 0, 2))
        system = MoonSystem([moon1, moon2, moon3])
        system.apply_velocities()
        self.assertEqual(Position(2, 3, 4), moon1.position)
        self.assertEqual(Position(5, 4, 3), moon2.position)
        self.assertEqual(Position(1, 3, 5), moon3.position)

    def test_time_step(self):
        moon1 = Moon(Position(1, 2, 3), Velocity())
        moon2 = Moon(Position(2, 2, 5), Velocity())
        moon3 = Moon(Position(6, 2, 3), Velocity())
        system = MoonSystem([moon1, moon2, moon3])
        system.time_step()
        self.assertEqual(Velocity(2, 0, 1), moon1.velocity)
        self.assertEqual(Velocity(0, 0, -2), moon2.velocity)
        self.assertEqual(Velocity(-2, 0, 1), moon3.velocity)
        self.assertEqual(Position(3, 2, 4), moon1.position)
        self.assertEqual(Position(2, 2, 3), moon2.position)
        self.assertEqual(Position(4, 2, 4), moon3.position)

    def test_get_energy(self):
        moon = Moon(Position(3, -1, 2), Velocity(-2, -5, 3))
        self.assertEqual(16, moon.get_energy())

    def test_total_energy(self):
        moon1 = Moon(Position(1, 1, 1), Velocity(1, 2, 3))
        moon2 = Moon(Position(2, 2, 2), Velocity(3, 2, 1))
        moon3 = Moon(Position(3, 3, 3), Velocity(-2, 0, 2))
        system = MoonSystem([moon1, moon2, moon3])
        self.assertEqual(3 + 6 + 6 + 6 + 9 + 4, system.total_energy())

    def test_from_string(self):
        moon = Moon.from_string("<x=-1, y=0, z=2>")
        self.assertEqual(Position(-1, 0, 2), moon.position)

    def test_from_string_system(self):
        s = """
            <x=-1, y=0, z=2>
            <x=2, y=-10, z=-7>
            <x=4, y=-8, z=8>
            <x=3, y=5, z=-1>
        """
        system = MoonSystem.from_string(s)
        self.assertEqual(Position(-1, 0, 2), system.moons[0].position)
        self.assertEqual(Position(2, -10, -7), system.moons[1].position)
        self.assertEqual(Position(4, -8, 8), system.moons[2].position)
        self.assertEqual(Position(3, 5, -1), system.moons[3].position)


if __name__ == "__main__":
    unittest.main()
