from math import prod


def check_for_tree_on_grid(grid, x, y):
    grid_width = len(grid[0])
    return grid[y][x % grid_width] == "#"


def check_path(grid, x_step, y_step):
    x = 0
    y = 0
    x += x_step
    y += y_step
    trees_encountered = 0
    while y < len(grid):
        if check_for_tree_on_grid(grid, x, y):
            trees_encountered += 1
        x += x_step
        y += y_step
    return trees_encountered


def check_all_paths(grid):
    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_list = [check_path(grid, path[0], path[1]) for path in paths]
    print(trees_list)
    return prod(trees_list)
