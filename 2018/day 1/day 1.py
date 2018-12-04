def day_1_a(frequency_shifts):
    """
    :param frequency_shifts: New-line or comma-delimited list of numbers. E.g. -2, +1, -3
    :return:
    """

    frequency_shifts = frequency_shifts.replace('\n', ',').split(',')

    def freq_fix(f):
        try:
            return int(f.strip())
        except ValueError:
            return 0

    return sum(map(freq_fix, frequency_shifts))


assert day_1_a("+1, -2, +3, +1") == 3
assert day_1_a("+1, +1, +1") == 3
assert day_1_a("+1, +1, -2") == 0
assert day_1_a("-1, -2, -3") == -6
with open("day 1 a.input") as f:
    print(day_1_a(f.read()))


def day_1_b(frequency_shifts):
    """
    :param frequency_shifts: New-line or comma-delimited list of numbers. E.g. -2, +1, -3
    :return:
    """

    frequency_shifts = frequency_shifts.replace('\n', ',').split(',')
    visited_frequencies = {0}
    total = 0

    def freq_fix(f):
        try:
            return int(f.strip())
        except ValueError:
            return 0

    while True:
        for f in frequency_shifts:
            total += freq_fix(f)
            if total in visited_frequencies:
                return total
            visited_frequencies.add(total)


assert day_1_b("+1, -2, +3, +1") == 2
assert day_1_b("+1, -1") == 0
assert day_1_b("+3, +3, +4, -2, -4") == 10
assert day_1_b("-6, +3, +8, +5, -6") == 5
assert day_1_b("+7, +7, -2, -7, -4") == 14
with open("day 1 a.input") as f:
    print(day_1_b(f.read()))
