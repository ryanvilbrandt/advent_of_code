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
        is_safe = False
        failed_index = check_safety(line)
        if failed_index is not None:
            copy = line.copy()
            del copy[failed_index - 1]
            if check_safety(copy) is None:
                is_safe = True
            else:
                copy = line.copy()
                del copy[failed_index]
                if check_safety(copy) is None:
                    is_safe = True
                else:
                    # Last option is that the "increasing" value was set wrong from the beginning.
                    # Check one more time with the first value removed.
                    copy = line.copy()
                    del copy[0]
                    if check_safety(copy) is None:
                        is_safe = True
        else:
            is_safe = True
        clints_is_safe = is_safe_with_damper(line)
        assert clints_is_safe == is_safe
        if is_safe:
            score += 1
    return score


# Stolen from Clint to find failed cases
def is_safe(levels: list[int]) -> bool:
    # We calculate the deltas first so we can operate directly on them
    deltas = [y - x for x, y in zip(levels[:-1], levels[1:])]
    # Grab the sign of the first element so we can compare it later
    first_sign = (deltas[0] >= 0)
    # Apply the rules: the difference has to be between 1 and 3 and the sign has to be constant
    return all(1 <= abs(x) <= 3 and (x >= 0) == first_sign for x in deltas)


def is_safe_with_damper(levels: list[int]):
    # Generator that produces variations a list with one element removed
    variations = ([x for i, x in enumerate(levels) if i != to_drop] for to_drop in range(len(levels)))
    # Using any() shortcuts if it finds a single one that works
    return any(is_safe(x) for x in variations)