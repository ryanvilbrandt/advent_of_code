def check_number(n: int):
    num_list = list(str(n))
    num_set = set(num_list)
    if not len(num_list) > len(num_set):
        return False
    if not sorted(num_list) == num_list:
        return False
    for i in num_set:
        if num_list.count(i) == 2:
            return True
    return False


def count_matches(start, stop):
    matches = []
    for i in range(start, stop + 1):
        if check_number(i):
            matches.append(i)
    return len(matches)


assert check_number(122345)
assert not check_number(111123)
assert not check_number(135679)
assert not check_number(111111)
assert not check_number(223450)
assert not check_number(123789)

assert check_number(112233)
assert not check_number(123444)
assert check_number(111122)

print(count_matches(240920, 789857))
