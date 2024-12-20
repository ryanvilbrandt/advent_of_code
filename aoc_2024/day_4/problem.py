def find_all_xmas(grid: list[list[str]]) -> int:
    count = 0
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == "X":
                count += find_xmas(grid, x, y)
    return count


def find_xmas(grid: list[list[str]], x: int, y: int) -> int:
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    count = 0
    for go_x, go_y in directions:
        if get_string(grid, x, y, go_x, go_y) == "XMAS":
            count += 1
    return count


def get_string(grid: list[list[str]], x: int, y: int, go_x: int, go_y: int, string_len: int = 4) -> str:
    s = grid[y][x]
    # print_grid(grid, x, y)
    for _ in range(string_len - 1):
        x += go_x
        y += go_y
        # print_grid(grid, x, y)
        if x < 0 or y < 0:
            return ""
        try:
            s += grid[y][x]
        except IndexError:
            return ""
    return s


def print_grid(grid: list[list[str]], coords: list[tuple[int, int]]):
    print("")
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if (x, y) in coords:
                sep = "["
            elif (x - 1, y) in coords:
                sep = "]"
            else:
                sep = " "
            print(sep, end="")
            print(cell, end="")
        print("")


def find_all_x_mas(grid: list[list[str]]) -> int:
    count = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == "A":
                # print(x, y)
                corners = get_corners(grid, x, y)
                if sorted(corners) == ["M", "M", "S", "S"]:
                    # Check for special case where Ms and Ss are opposite each other
                    if corners != ["M", "S", "M", "S"] and corners != ["S", "M", "S", "M"]:
                        count += 1
                        # print("Count increased")
                pass
    return count


def get_corners(grid: list[list[str]], x: int, y: int) -> list[str]:
    directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    corners = []
    coords = [(x, y)]
    for go_x, go_y in directions:
        new_x, new_y = x + go_x, y + go_y
        coords.append((new_x, new_y))
        if new_x < 0 or new_y < 0:
            # print_grid(grid, coords)
            return []
        try:
            corners.append(grid[new_y][new_x])
        except IndexError:
            # print_grid(grid, coords)
            return []
    # print_grid(grid, coords)
    return corners
