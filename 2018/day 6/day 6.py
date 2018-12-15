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
    print(start_x, end_x, start_y, end_y)
    for i, p in enumerate(point_dict):
        print(i, p)
        map[p[1]][p[0]] = labels[i]
        for q in point_dict[p]:
            map[q[1]][q[0]] = labels[i].lower()
    for row in map:
        print("".join(row))


def build_map(in_str):
    processed_input = preprocess_input(in_str)
    print(processed_input)
    # Init area dict
    area_dict = OrderedDict()
    for p in processed_input:
        area_dict[p] = []
    print(area_dict)
    # Determine the borders of the map
    x_coords, y_coords = list(zip(*area_dict.keys()))
    start_x = min(x_coords)
    end_x = max(x_coords)
    start_y = min(y_coords)
    end_y = max(y_coords)
    print_map(area_dict, start_x, end_x, start_y, end_y)
    print()
    # Check closest point for all points in the given area
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            test_point = x, y
            # Don't test main points
            if test_point in area_dict.keys():
                continue
            closest_point = find_closest_point(test_point, area_dict)
            if closest_point:
                area_dict[closest_point].append(test_point)
    print(dict(area_dict))
    print_map(area_dict, start_x, end_x, start_y, end_y)


build_map(day_6_example)