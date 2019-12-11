from collections import defaultdict
from math import inf
from typing import Tuple, List, Dict


def str_to_grid(s):
    return [list(row.strip()) for row in s.strip().split("\n")]


def get_coords(grid) -> List[Tuple[int, int]]:
    coords = []
    for y, row in enumerate(grid):
        for x, asteroid in enumerate(row):
            if asteroid == "#":
                coords.append((x, y))
    return coords


def count_visible_asteroids(origin: Tuple[int, int], coords_list: List[Tuple[int, int]]):
    buckets = SlopeBuckets()
    buckets.sort_points_into_buckets(origin, coords_list)
    return buckets.count_buckets()


def get_all_asteroid_views(s):
    coords_list = get_coords(str_to_grid(s))
    views_dict = {}
    for coords in coords_list:
        views_dict[coords] = count_visible_asteroids(coords, coords_list)
    return views_dict


def get_best_view(s):
    views = get_all_asteroid_views(s)
    return max(views.items(), key=lambda x: x[1])


def shoot_all_asteroids(s, origin: Tuple[int, int]):
    coords_list = get_coords(str_to_grid(s))
    buckets = SlopeBuckets()
    buckets.sort_points_into_buckets(origin, coords_list)
    buckets.sort_lists_in_buckets(origin)
    return buckets.shoot_asteroids()


class SlopeBuckets:

    def __init__(self):
        self.left = defaultdict(list)
        self.right = defaultdict(list)

    def put_slope_in_bucket(self, origin: Tuple[int, int], target: Tuple[int, int]):
        if origin == target:
            return
        x = target[0] - origin[0]
        y = target[1] - origin[1]
        if x == 0:
            # If it's straight up, put it in the right section
            if y > 0:
                self.left[-inf].append(target)
            else:
                self.right[-inf].append(target)
        elif x < 0:
            self.left[y / x].append(target)
        elif x > 0:
            self.right[y / x].append(target)
        else:
            raise Exception("HALT AND CATCH FIRE")

    def count_buckets(self):
        return len(self.left) + len(self.right)

    def sort_points_into_buckets(self, origin: Tuple[int, int], coords_list: List[Tuple[int, int]]):
        for coords in coords_list:
            self.put_slope_in_bucket(origin, coords)

    def sort_lists_in_buckets(self, origin: Tuple[int, int]):
        """
        Go through each asteroid in the same slope value and sort by distance to the origin.
        We can use manhattan distance to save processing power.
        :param origin:
        :return:
        """
        self.sort_bucket_list(origin, self.left)
        self.sort_bucket_list(origin, self.right)

    def sort_bucket_list(self, origin: Tuple[int, int], bucket: Dict[float, List[Tuple[int, int]]]):
        def sort_key(coord: Tuple[int, int]):
            return abs(coord[0] - origin[0]) + abs(coord[1] - origin[1])
        for slope, coords_list in bucket.items():
            coords_list.sort(key=sort_key)

    def shoot_asteroids(self):
        asteroid_list = []
        while self.count_buckets() > 0:
            for bucket in [self.right, self.left]:
                for k in sorted(bucket.keys()):
                    if bucket[k]:
                        asteroid_list.append(bucket[k].pop(0))
                        if not bucket[k]:
                            del bucket[k]
        return asteroid_list
