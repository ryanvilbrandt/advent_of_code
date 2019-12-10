from typing import Tuple, List


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
    buckets.sort_points(origin, coords_list)
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


class SlopeBuckets:

    def __init__(self):
        self.left_or_right = set()
        self.top = set()
        self.bottom = set()

    def put_slope_in_bucket(self, origin: Tuple[int, int], target: Tuple[int, int]):
        if origin == target:
            return
        x = target[0] - origin[0]
        y = target[1] - origin[1]
        if y == 0:
            self.left_or_right.add("left" if x < 0 else "right")
        elif y < 0:
            self.top.add(x / y)
        elif y > 0:
            self.bottom.add(x / y)
        else:
            raise Exception("HALT AND CATCH FIRE")

    def count_buckets(self):
        return len(self.left_or_right) + len(self.top) + len(self.bottom)

    def sort_points(self, origin: Tuple[int, int], coords_list: List[Tuple[int, int]]):
        for coords in coords_list:
            self.put_slope_in_bucket(origin, coords)
