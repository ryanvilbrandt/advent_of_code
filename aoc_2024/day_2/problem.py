from typing import Optional


def get_safety_score(grid: list[list[int]]) -> int:
    score = 0
    for line in grid:
        if check_safety(line) is None:
            score += 1
    return score


def check_safety(line: list[int]) -> Optional[int]:
    increasing = None
    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]
        if increasing is None:
            increasing = diff > 0
        elif increasing != (diff > 0):
            return i
        if not (1 <= abs(diff) <= 3):
            return i
    else:
        return None


def get_safety_score_with_dampening(grid: list[list[int]]) -> int:
    score = 0
    for line in grid:
        failed_index = check_safety(line)
        if failed_index is not None:
            copy = line.copy()
            del copy[failed_index - 1]
            if check_safety(copy) is None:
                continue
            copy = line.copy()
            del copy[failed_index]
            if check_safety(copy) is None:
                continue
        score += 1
    return score
