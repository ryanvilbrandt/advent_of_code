knot_hash = __import__("knot_hash")
calc_hash = knot_hash.calc_hash


def hash_to_bin(hash):
    return "".join(["{:>04b}".format(int(c, 16)) for c in hash])


def build_grid(my_input):
    grid = []
    for i in range(128):
        hash = calc_hash(my_input + "-" + str(i))
        hash = hash_to_bin(hash)
        hash = hash.replace("1", "#").replace("0", ".")
        grid.append(hash)
        # print(hash[:8])
        # if i >= 8:
        #     return grid
    return grid


def count_squares(grid):
    return sum([str(row).count("#") for row in grid])


def count_regions(grid):
    # Turn grid into a list of characters
    grid = [[c for c in line] for line in grid]

    regions = 0
    squares = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "#":
                # print("Found one!")
                regions += 1
                squares += remove_region(grid, x, y)
    return regions, squares


def remove_region(grid, x, y):
    """
    Removes a region starting at a particular index from the grid. Uses recursion to find the region.
    :param grid: list of list of str
    :return: Number of squares in the region that was removed
    """
    # Check for out of bounds
    if x < 0 or y < 0:
        return 0
    try:
        char = grid[y][x]
    except IndexError:
        return 0

    # Check if block is already marked (#)
    if char == ".":
        return 0

    # Replace character with period
    # print(x, y)
    grid[y][x] = "."
    squares = 1

    # Check surrounding blocks (cardinal directions only)
    squares += remove_region(grid, x, y - 1)
    squares += remove_region(grid, x - 1, y)
    squares += remove_region(grid, x + 1, y)
    squares += remove_region(grid, x, y + 1)
    return squares


# a = "flqrgnkx"
a = "jzgqcdpd"

# print(count_squares(build_grid(a)))
print(count_regions(build_grid(a)))
