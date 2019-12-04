from typing import Dict


def build_wire_path(directions: str):
    direction_list = directions.split(",")
    point_dict = {}
    current_point = [0, 0]
    steps = 0
    for d in direction_list:
        direction, distance = d[0].upper(), int(d[1:])
        for _ in range(distance):
            if direction == "L":
                current_point[0] -= 1
            elif direction == "R":
                current_point[0] += 1
            elif direction == "D":
                current_point[1] -= 1
            elif direction == "U":
                current_point[1] += 1
            else:
                raise Exception("HALT AND CATCH FIRE")
            steps += 1
            key = tuple(current_point[:])
            if key not in point_dict:
                point_dict[key] = steps
    return point_dict


def calculate_closest_distance(left_points: Dict[tuple, int], right_points: Dict[tuple, int]):
    intersections = set(left_points.keys()).intersection(right_points.keys())
    manhattan_distances = []
    steps_taken = []
    for i in intersections:
        manhattan_distances.append(abs(i[0]) + abs(i[1]))
        steps_taken.append(left_points[i] + right_points[i])
    return min(manhattan_distances), min(steps_taken)


def follow_wires(text):
    left_wire, right_wire = text.split("\n")
    left_points = build_wire_path(left_wire)
    right_points = build_wire_path(right_wire)
    return calculate_closest_distance(left_points, right_points)


assert follow_wires("""R8,U5,L5,D3
U7,R6,D4,L4""") == (6, 30)
assert follow_wires("""R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""") == (159, 610)
assert follow_wires("""R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7""") == (135, 410)

with open("day 3.input") as f:
    distance, steps = follow_wires(f.read())
    print(distance)
    print(steps)
