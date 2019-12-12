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
        self.assertEqual(6 * 10, moon.get_energy())

    def test_total_energy(self):
        moon1 = Moon(Position(1, 1, 1), Velocity(1, 2, 3))
        moon2 = Moon(Position(2, 2, 2), Velocity(3, 2, 1))
        moon3 = Moon(Position(3, 3, 3), Velocity(-2, 0, 2))
        system = MoonSystem([moon1, moon2, moon3])
        self.assertEqual(3 * 6 + 6 * 6 + 9 * 4, system.total_energy())

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

    def test_part_12_example_1(self):
        s = """
            <x=-1, y=0, z=2>
            <x=2, y=-10, z=-7>
            <x=4, y=-8, z=8>
            <x=3, y=5, z=-1>
        """
        system = MoonSystem.from_string(s)
        self.assertEqual(Position(-1, 0, 2), system.moons[0].position)
        self.assertEqual(Velocity(0, 0, 0), system.moons[0].velocity)
        self.assertEqual(Position(2, -10, -7), system.moons[1].position)
        self.assertEqual(Velocity(0, 0, 0), system.moons[1].velocity)
        self.assertEqual(Position(4, -8, 8), system.moons[2].position)
        self.assertEqual(Velocity(0, 0, 0), system.moons[2].velocity)
        self.assertEqual(Position(3, 5, -1), system.moons[3].position)
        self.assertEqual(Velocity(0, 0, 0), system.moons[3].velocity)

        # Time step 1
        system.time_step()
        self.assertEqual(Position(2, -1, 1), system.moons[0].position)
        self.assertEqual(Velocity(3, -1, -1), system.moons[0].velocity)
        self.assertEqual(Position(3, -7, -4), system.moons[1].position)
        self.assertEqual(Velocity(1, 3, 3), system.moons[1].velocity)
        self.assertEqual(Position(1, -7, 5), system.moons[2].position)
        self.assertEqual(Velocity(-3, 1, -3), system.moons[2].velocity)
        self.assertEqual(Position(2, 2, 0), system.moons[3].position)
        self.assertEqual(Velocity(-1, -3, 1), system.moons[3].velocity)

        # Time step 2
        system.time_step()
        self.assertEqual(Position(5, -3, -1), system.moons[0].position)
        self.assertEqual(Velocity(3, -2, -2), system.moons[0].velocity)
        self.assertEqual(Position(1, -2, 2), system.moons[1].position)
        self.assertEqual(Velocity(-2, 5, 6), system.moons[1].velocity)
        self.assertEqual(Position(1, -4, -1), system.moons[2].position)
        self.assertEqual(Velocity(0, 3, -6), system.moons[2].velocity)
        self.assertEqual(Position(1, -4, 2), system.moons[3].position)
        self.assertEqual(Velocity(-1, -6, 2), system.moons[3].velocity)

        # Time step 3
        system.time_step()
        self.assertEqual(Position(5, -6, -1), system.moons[0].position)
        self.assertEqual(Velocity(0, -3, 0), system.moons[0].velocity)
        self.assertEqual(Position(0, 0, 6), system.moons[1].position)
        self.assertEqual(Velocity(-1, 2, 4), system.moons[1].velocity)
        self.assertEqual(Position(2, 1, -5), system.moons[2].position)
        self.assertEqual(Velocity(1, 5, -4), system.moons[2].velocity)
        self.assertEqual(Position(1, -8, 2), system.moons[3].position)
        self.assertEqual(Velocity(0, -4, 0), system.moons[3].velocity)

        # Time step 4
        system.time_step()
        self.assertEqual(Position(2, -8, 0), system.moons[0].position)
        self.assertEqual(Velocity(-3, -2, 1), system.moons[0].velocity)
        self.assertEqual(Position(2, 1, 7), system.moons[1].position)
        self.assertEqual(Velocity(2, 1, 1), system.moons[1].velocity)
        self.assertEqual(Position(2, 3, -6), system.moons[2].position)
        self.assertEqual(Velocity(0, 2, -1), system.moons[2].velocity)
        self.assertEqual(Position(2, -9, 1), system.moons[3].position)
        self.assertEqual(Velocity(1, -1, -1), system.moons[3].velocity)

        # Time step 5
        system.time_step()
        self.assertEqual(Position(-1, -9, 2), system.moons[0].position)
        self.assertEqual(Velocity(-3, -1, 2), system.moons[0].velocity)
        self.assertEqual(Position(4, 1, 5), system.moons[1].position)
        self.assertEqual(Velocity(2, 0, -2), system.moons[1].velocity)
        self.assertEqual(Position(2, 2, -4), system.moons[2].position)
        self.assertEqual(Velocity(0, -1, 2), system.moons[2].velocity)
        self.assertEqual(Position(3, -7, -1), system.moons[3].position)
        self.assertEqual(Velocity(1, 2, -2), system.moons[3].velocity)

        # Time step 6
        system.time_step()
        self.assertEqual(Position(-1, -7, 3), system.moons[0].position)
        self.assertEqual(Velocity(0, 2, 1), system.moons[0].velocity)
        self.assertEqual(Position(3, 0, 0), system.moons[1].position)
        self.assertEqual(Velocity(-1, -1, -5), system.moons[1].velocity)
        self.assertEqual(Position(3, -2, 1), system.moons[2].position)
        self.assertEqual(Velocity(1, -4, 5), system.moons[2].velocity)
        self.assertEqual(Position(3, -4, -2), system.moons[3].position)
        self.assertEqual(Velocity(0, 3, -1), system.moons[3].velocity)

        # Time step 7
        system.time_step()
        self.assertEqual(Position(2, -2, 1), system.moons[0].position)
        self.assertEqual(Velocity(3, 5, -2), system.moons[0].velocity)
        self.assertEqual(Position(1, -4, -4), system.moons[1].position)
        self.assertEqual(Velocity(-2, -4, -4), system.moons[1].velocity)
        self.assertEqual(Position(3, -7, 5), system.moons[2].position)
        self.assertEqual(Velocity(0, -5, 4), system.moons[2].velocity)
        self.assertEqual(Position(2, 0, 0), system.moons[3].position)
        self.assertEqual(Velocity(-1, 4, 2), system.moons[3].velocity)

        # Time step 8
        system.time_step()
        self.assertEqual(Position(5, 2, -2), system.moons[0].position)
        self.assertEqual(Velocity(3, 4, -3), system.moons[0].velocity)
        self.assertEqual(Position(2, -7, -5), system.moons[1].position)
        self.assertEqual(Velocity(1, -3, -1), system.moons[1].velocity)
        self.assertEqual(Position(0, -9, 6), system.moons[2].position)
        self.assertEqual(Velocity(-3, -2, 1), system.moons[2].velocity)
        self.assertEqual(Position(1, 1, 3), system.moons[3].position)
        self.assertEqual(Velocity(-1, 1, 3), system.moons[3].velocity)

        # Time step 9
        system.time_step()
        self.assertEqual(Position(5, 3, -4), system.moons[0].position)
        self.assertEqual(Velocity(0, 1, -2), system.moons[0].velocity)
        self.assertEqual(Position(2, -9, -3), system.moons[1].position)
        self.assertEqual(Velocity(0, -2, 2), system.moons[1].velocity)
        self.assertEqual(Position(0, -8, 4), system.moons[2].position)
        self.assertEqual(Velocity(0, 1, -2), system.moons[2].velocity)
        self.assertEqual(Position(1, 1, 5), system.moons[3].position)
        self.assertEqual(Velocity(0, 0, 2), system.moons[3].velocity)

        # Time step 10
        system.time_step()
        self.assertEqual(Position(2, 1, -3), system.moons[0].position)
        self.assertEqual(Velocity(-3, -2, 1), system.moons[0].velocity)
        self.assertEqual(Position(1, -8, 0), system.moons[1].position)
        self.assertEqual(Velocity(-1, 1, 3), system.moons[1].velocity)
        self.assertEqual(Position(3, -6, 1), system.moons[2].position)
        self.assertEqual(Velocity(3, 2, -3), system.moons[2].velocity)
        self.assertEqual(Position(2, 0, 4), system.moons[3].position)
        self.assertEqual(Velocity(1, -1, -1), system.moons[3].velocity)

        self.assertEqual(36 + 45 + 80 + 18, system.total_energy())

    def test_day_12_example_2(self):
        s = """
            <x=-8, y=-10, z=0>
            <x=5, y=5, z=10>
            <x=2, y=-7, z=3>
            <x=9, y=-8, z=-3>
        """
        system = MoonSystem.from_string(s)
        for _ in range(100):
            system.time_step()
        self.assertEqual(290 + 608 + 574 + 468, system.total_energy())

    def test_day_12_part_1(self):
        with open("input.text") as f:
            system = MoonSystem.from_string(f.read())
        for _ in range(1000):
            system.time_step()
        self.assertEqual(9999, system.total_energy())

    def test_hash(self):
        s = """
            <x=1, y=2, z=3>
            <x=3, y=2, z=1>
        """
        system = MoonSystem.from_string(s)
        print(system)
        print(system.get_hash())
        system.time_step()
        print(system)
        print(system.get_hash())

    def test_find_factors(self):
        self.assertEqual([2, 2, 2, 2], find_factors(16))
        self.assertEqual([2, 2, 2, 3], find_factors(24))
        self.assertEqual([2, 3, 3], find_factors(18))
        self.assertEqual([2, 2, 7], find_factors(28))
        self.assertEqual([2, 2, 11], find_factors(44))
        print(find_factors(4686774924))

    def test_find_lcm(self):
        self.assertEqual(2772, find_lcm([18, 28, 44]))

    def test_loop_example_1(self):
        s = """
            <x=-1, y=0, z=2>
            <x=2, y=-10, z=-7>
            <x=4, y=-8, z=8>
            <x=3, y=5, z=-1>
        """
        system = MoonSystem.from_string(s)
        loop_nums = system.find_loop(2772)
        self.assertEqual(2772, find_lcm(loop_nums))

    def test_loop_example_2(self):
        s = """
            <x=-8, y=-10, z=0>
            <x=5, y=5, z=10>
            <x=2, y=-7, z=3>
            <x=9, y=-8, z=-3>
        """
        system = MoonSystem.from_string(s)
        loop_nums = system.find_loop(10000)
        self.assertEqual(4686774924, find_lcm(loop_nums))

    def test_day_12_part_2(self):
        with open("input.text") as f:
            system = MoonSystem.from_string(f.read())
        loop_nums = system.find_loop(1000000)
        self.assertEqual(282399002133976, find_lcm(loop_nums))


if __name__ == "__main__":
    unittest.main()
