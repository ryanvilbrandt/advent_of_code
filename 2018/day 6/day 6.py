from collections import OrderedDict

day_6_example = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

labels = [chr(ord('A') + i) for i in range(26)]


def preprocess_input(in_str):
    processed_input = []
    for x in in_str.split('\n'):
        if not x:
            continue
        processed_input.append(tuple(map(int, x.split(', '))))
    return processed_input


def find_closest_point(test_point, point_dict):
    closest_point = None
    closest_distance = None
    for p in point_dict:
        distance = abs(p[0] - test_point[0]) + abs(p[1] - test_point[1])
        if closest_distance is None or distance < closest_distance:
            closest_point = p
            closest_distance = distance
        elif distance == closest_distance:
            closest_point = None
    return closest_point


def print_map(point_dict, start_x, end_x, start_y, end_y):
    """
    :param point_dict: Dict of all points and the other points they "own". Must be <=26
    :return:
    """
    map = [['.' for x in range(start_x, end_x)] for y in range(start_y, end_y)]
    for i, p in enumerate(point_dict):
        map[p[1] - start_y][p[0] - start_x] = labels[i]
        for q in point_dict[p]:
            map[q[1] - start_y][q[0] - start_x] = labels[i].lower()
    for row in map:
        print("".join(row))


def build_map(in_str):
    processed_input = preprocess_input(in_str)
    # Init area dict
    area_dict = OrderedDict()
    for p in processed_input:
        area_dict[p] = []
    # Determine the borders of the map
    x_coords, y_coords = list(zip(*area_dict.keys()))
    start_x = min(x_coords) - 1
    end_x = max(x_coords) + 1
    start_y = min(y_coords) - 1
    end_y = max(y_coords) + 1
    # Check closest point for all points in the given area
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            test_point = x, y
            # Don't test main points
            if test_point in area_dict.keys():
                continue
            closest_point = find_closest_point(test_point, area_dict)
            if closest_point:
                area_dict[closest_point].append(test_point)
    # Count up max area
    # Check for infinite areas by excluding all points whose area falls on the boundary
    max_area = 0
    for i, p in enumerate(area_dict):
        x_coords, y_coords = list(zip(*area_dict[p]))
        if not ((min(x_coords) == start_x) or
                (max(x_coords) == end_x) or
                (min(y_coords) == start_y) or
                (max(y_coords) == end_y)):
            area_count = len(area_dict[p]) + 1
            if area_count > max_area:
                max_area = area_count
    return max_area


assert build_map(day_6_example) == 17
with open("day 6.input") as f:
    print(build_map(f.read()))


def find_total_distance(test_point, coord_list):
    return sum([abs(p[0] - test_point[0]) + abs(p[1] - test_point[1])
                for p in coord_list])


def find_safe_region(in_str, threshold):
    processed_input = preprocess_input(in_str)
    # Determine the borders of the map
    x_coords, y_coords = list(zip(*processed_input))
    start_x = min(x_coords) - 1
    end_x = max(x_coords) + 1
    start_y = min(y_coords) - 1
    end_y = max(y_coords) + 1
    # Check total distance for all points in the given area
    region_size = 0
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            test_point = x, y
            total_distance = find_total_distance(test_point, processed_input)
            if total_distance < threshold:
                region_size += 1
    return region_size


assert find_safe_region(day_6_example, 32) == 16
with open("day 6.input") as f:
    print(find_safe_region(f.read(), 10000))
