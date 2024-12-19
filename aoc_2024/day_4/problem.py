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


def print_grid(grid: list[list[str]], cursor_x: int, cursor_y: int):
    print("")
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            print(cell, end="")
            sep = " "
            if y == cursor_y:
                if x == cursor_x - 1:
                    sep = "["
                elif x == cursor_x:
                    sep = "]"
            print(sep, end="")
        print("")


def find_all_x_mas(grid: list[list[str]]) -> int:
    count = 0
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == "A":
                corners = get_corners(grid, x, y)
                if sorted(corners) == ["M", "M", "S", "S"]:
                    count += 1
    return count


def get_corners(grid: list[list[str]], x: int, y: int) -> list[str]:
    directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    corners = []
    for go_x, go_y in directions:
        new_x, new_y = x + go_x, y + go_y
        if new_x < 0 or new_y < 0:
            return []
        try:
            corners.append(grid[new_y][new_x])
        except IndexError:
            return []
    return corners
