from math import ceil
from typing import Tuple

import numpy
from numpy import ndarray

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
CLEAN, WEAKENED, INFECTED, FLAGGED = 0, 1, 2, 3


def text_to_array(text: str) -> ndarray:
    d = {'.': CLEAN, 'W': WEAKENED, '#': INFECTED, 'F': FLAGGED}
    array = [[d[c] for c in line] for line in text.strip('\n').split('\n')]
    numpy_array = numpy.array(array)
    # print(numpy_array)
    # numpy_array = pad_array(numpy_array, 500)
    # print(numpy_array)
    return numpy_array


def pad_array(array, padding):
    rows, columns = array.shape
    padded_array = numpy.zeros((rows + padding * 2, columns + padding * 2), dtype='int32')
    padded_array[padding:(rows + padding), padding:columns + padding] = array
    return padded_array


def find_center(grid: ndarray) -> Tuple[int, int]:
    """
    :param grid:
    :return: (y, x)
    """
    rows, columns = grid.shape
    print("Center:", int(rows / 2), int(columns / 2))
    return int(rows / 2), int(columns / 2)


def check_loc(grid: ndarray, virus_loc):
    y, x = virus_loc
    rows, columns = grid.shape
    return 0 <= y < rows and 0 <= x < columns


def burst(grid: ndarray, virus_loc: Tuple[int, int], virus_facing: int, infection_count: int):
    """
    :param grid:
    :param virus_loc: (y, x)
    :param virus_facing:
    :return:
    """
    if not check_loc(grid, virus_loc):
        grid = pad_array(grid, 10)
        virus_loc = virus_loc[0] + 10, virus_loc[1] + 10

    y, x = virus_loc
    cell = grid[y][x]

    # Turn based on infection state
    if cell == CLEAN:
        turn = -1
    elif cell == WEAKENED:
        turn = 0
    elif cell == INFECTED:
        turn = 1
    elif cell == FLAGGED:
        turn = 2
    else:
        raise Exception("Bad state")
    virus_facing = (virus_facing + turn) % 4
    # Advance infection state
    grid[y][x] = (cell + 1) % 4
    # If infected, increase infection count
    if grid[y][x] == INFECTED:
        infection_count += 1
    # Move virus forward
    if virus_facing == NORTH:
        virus_loc = (y - 1, x)
    elif virus_facing == EAST:
        virus_loc = (y, x + 1)
    elif virus_facing == SOUTH:
        virus_loc = (y + 1, x)
    elif virus_facing == WEST:
        virus_loc = (y, x - 1)
    return grid, virus_loc, virus_facing, infection_count


def print_grid(grid: ndarray, virus_loc=None):
    if virus_loc is None:
        virus_loc = (-1, -1)
    print()
    for y, line in enumerate(grid):
        print("[" if virus_loc == (y, 0) else " ", end='')
        for x, c in enumerate(line):
            d = {CLEAN: '.', WEAKENED: 'W', INFECTED: '#', FLAGGED: 'F'}
            print(d[c], end='')
            if (y, x) == virus_loc:
                print("]", end='')
            elif (y, x + 1) == virus_loc:
                print("[", end='')
            else:
                print(" ", end='')
        print()


def run_virus(text, runs=1e7):
    runs = int(runs)
    grid = text_to_array(text)
    virus_loc = find_center(grid)
    virus_facing = NORTH
    infection_count = 0

    # print_grid(grid, virus_loc)
    for i in range(1, runs):
        if i % 5e5 == 0:
            print(f'{i} / {runs}')
        grid, virus_loc, virus_facing, infection_count = burst(grid, virus_loc, virus_facing, infection_count)
        # print_grid(grid, virus_loc)
        # print("Infection count:", infection_count)
    print(infection_count)


def count_infected(grid):
    unique, counts = numpy.unique(grid, return_counts=True)
    infected_dict = dict(zip(unique, counts))
    print(infected_dict)
    return infected_dict[INFECTED]



# with open('example.input') as f:
# with open('test.input') as f:
with open('day 22.input') as f:
    a = f.read()

run_virus(a)
