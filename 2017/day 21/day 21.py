STARTING_PATTERN = [
    ".#.",
    "..#",
    "###"
]
# STARTING_PATTERN = [
#     ".##",
#     "#.#",
#     "..#"
# ]
# STARTING_PATTERN = [
#     "###",
#     "#..",
#     ".#."
# ]
# STARTING_PATTERN = [
#     "#..",
#     "#.#",
#     "##."
# ]
# STARTING_PATTERN = [
#     "....",
#     "....",
#     "....",
#     "...."
# ]
# STARTING_PATTERN = [
#     "#..#",
#     "....",
#     "....",
#     "#..#"
# ]


def build_rules(text: str):
    text = text.strip('\n').split('\n')
    rules_list = []
    for line in text:
        before, after = line.split(' => ')
        rules_list.append((before.split('/'), after.split('/')))
    return rules_list


def find_matching_rule(grid, x, y, size, rules):
    for rule in rules:
        if compare_to_rule(grid, x, y, size, rule[0]):
            return rule[1]
    raise Exception(f"No pattern found for grid: {grid}")


def compare_to_rule(grid, x, y, size, rule):
    return (
        do_compare(grid, x, y, size, rule, orientation=0) or
        do_compare(grid, x, y, size, rule, orientation=90) or
        do_compare(grid, x, y, size, rule, orientation=180) or
        do_compare(grid, x, y, size, rule, orientation=270)
    )


def do_compare(grid, x, y, size, rule, orientation=0):
    """
    Does a comparison between a grid square and a rule.
    :param grid:
    :param x:
    :param y:
    :param size:
    :param rule:
    :param orientation: 0, 90, 180, or 270.
    :return:
    """
    # First check if the rule size matches the size of the subgrid we're comparing it to.
    if len(rule[0]) != size:
        return False
    # print(orientation)
    # print(grid)
    # print(rule)
    a, b = 0, 0
    for i in range(size):
        for j in range(size):
            if orientation == 0:
                a = y + i
                b = x + j
            elif orientation == 90:
                a = y + size - j - 1
                b = x + i
            elif orientation == 180:
                a = y + size - i - 1
                b = x + size - j - 1
            elif orientation == 270:
                a = y + j
                b = x + size - i - 1
            # print(i, j, a, b)
            if not grid[a][b] == rule[i][j]:
                return False
    return True


def append_horizontal_results(start, end):
    """
    Start and end are both list of lists, and we're appending end to start so that the grids they represent are
    sitting side by side.

    For example, if start is:
    ABCDEF
    HIJKLM
    NOPQRS

    And end is:
    123
    456
    789

    Then the result should be:
    ABCDEF123
    HIJKLM456
    NOPQRS789

    start and end must both have the same number of rows.

    :param start:
    :param end:
    :return:
    """
    new_grid = []
    for i, start_row in enumerate(start):
        new_grid.append(start_row + end[i])
    return new_grid


def process_grid(grid, rules):
    size = 2 if len(grid) % 2 == 0 else 3
    new_grid = []
    for y in range(0, len(grid), size):
        new_rows = [""] * (size + 1)
        for x in range(0, len(grid), size):
            match = find_matching_rule(grid, x, y, size, rules)
            new_rows = append_horizontal_results(
                new_rows,
                match
            )
        new_grid += new_rows
    return new_grid


def print_grid(grid):
    print("\n".join(grid))


def run_patterns(grid, rules, iterations=5):
    print_grid(grid)
    print()
    for i in range(iterations):
        grid = process_grid(grid, rules)
        print_grid(grid)
        print()
    return grid


with open("example_test.input") as f:
    a = f.read()
# with open("day 21.input") as f:
#     a = f.read()


rules = build_rules(a)
# print(rules)
# print(compare_to_rule(STARTING_PATTERN, 0, 0, 3, rules[1][0]))
print_grid(run_patterns(STARTING_PATTERN, rules))
