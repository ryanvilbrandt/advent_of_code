import re


class Particle:

    def __init__(self, name: str,
                 p_x: int, p_y: int, p_z:
            int, v_x: int, v_y: int, v_z:
            int, a_x: int, a_y: int, a_z: int):
        self.name = name
        self.p_x = p_x
        self.p_y = p_y
        self.p_z = p_z
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        self.a_x = a_x
        self.a_y = a_y
        self.a_z = a_z

    def tick(self):
        self.v_x += self.a_x
        self.v_y += self.a_y
        self.v_z += self.a_z
        self.p_x += self.v_x
        self.p_y += self.v_y
        self.p_z += self.v_z
        return (self.p_x, self.p_y, self.p_z)

    def get_distance(self, x=0, y=0, z=0):
        return abs(self.p_x - x) + abs(self.p_y - y) + abs(self.p_z - z)

    @staticmethod
    def make(name: str, text: str):
        regex = re.compile(r'p=<(-?[\d]+),(-?[\d]+),(-?[\d]+)>, '
                           r'v=<(-?[\d]+),(-?[\d]+),(-?[\d]+)>, '
                           r'a=<(-?[\d]+),(-?[\d]+),(-?[\d]+)>')
        m = re.match(regex, text)
        return Particle(name,
                        int(m.group(1)), int(m.group(2)), int(m.group(3)),
                        int(m.group(4)), int(m.group(5)), int(m.group(6)),
                        int(m.group(7)), int(m.group(8)), int(m.group(9)))

    def __str__(self):
        return f"Particle(name={self.name}, " \
               f"p=<{self.p_x},{self.p_y},{self.p_z}>, " \
               f"v=<{self.v_x},{self.v_y},{self.v_z}>, " \
               f"a=<{self.a_x},{self.a_y},{self.a_z}>)"

    def __repr__(self):
        return str(self)


def simulate_particles(text):
    text = text.strip('\n').split('\n')
    particles = [Particle.make(str(i), line) for i, line in enumerate(text)]

    # for p in particles:
    #     print(p)
    # print()

    closest_particle = (None, None)
    for _ in range(1000):
        smallest_distance = (None, None)
        for p in particles:
            p.tick()
            distance = p.get_distance()
            if smallest_distance[1] is None or distance < smallest_distance[1]:
                smallest_distance = (p, distance)
        if smallest_distance[0] != closest_particle[0]:
            closest_particle = smallest_distance
            print(closest_particle)


def smallest_accel(text):
    text = text.strip('\n').split('\n')
    particles = [Particle.make(str(i), line) for i, line in enumerate(text)]

    min_particle = None
    min_a = 99999
    for p in particles:
        a = abs(p.a_x) + abs(p.a_y) + abs(p.a_z)
        if a < min_a:
            min_a = a
            min_particle = p
    return min_particle


def simulate_particles_with_collision(text):
    text = text.strip('\n').split('\n')
    particles = [Particle.make(str(i), line) for i, line in enumerate(text)]

    # for p in particles:
    #     print(p)
    # print()

    for _ in range(1000):
        position_dict = {}
        collision_locations = set()
        for p in particles:
            pos = p.tick()
            # Get the list of particles at that position and add this particle to that position
            position_dict[pos] = position_dict.get(pos, []) + [p]
            # If the current position has more than one particle,
            # add it to collision locations to clean later
            if len(position_dict[pos]) > 1:
                collision_locations.add(pos)
        # Remove all particles that have collided
        for loc in collision_locations:
            for p in position_dict[loc]:
                particles.remove(p)
    print("Particle count:", len(particles))


# a = """
# p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
# p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>
# """
# with open("day 20.input") as f:
#     a = f.read()
#
#
# simulate_particles(a)
# print()
# print(smallest_accel(a))

# a = """
# p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
# p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
# p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
# p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
# """
with open("day 20.input") as f:
    a = f.read()

simulate_particles_with_collision(a)

