import re
from math import inf

from aoc_2020.common import text_to_list


def get_seat_id(seat_string):
    return int(re.sub(r"[BR]", "1", re.sub(r"[FL]", "0", seat_string)), 2)


def get_highest_and_lowest_seat_id(boarding_pass_list):
    min_seat_id = inf
    max_seat_id = -inf
    for seat_string in text_to_list(boarding_pass_list):
        seat_id = get_seat_id(seat_string)
        min_seat_id = min(min_seat_id, seat_id)
        max_seat_id = max(max_seat_id, seat_id)
    return min_seat_id, max_seat_id


def get_seat_id_list(boarding_pass_list):
    return sorted([get_seat_id(boarding_pass) for boarding_pass in text_to_list(boarding_pass_list)])


def get_expected_total(min_num, max_num):
    return (max_num * (max_num + 1) - (min_num - 1) * min_num) / 2


def get_missing_seat(boarding_pass_list):
    min_seat_id = inf
    max_seat_id = -inf
    total = 0
    for seat_string in text_to_list(boarding_pass_list):
        seat_id = get_seat_id(seat_string)
        min_seat_id = min(min_seat_id, seat_id)
        max_seat_id = max(max_seat_id, seat_id)
        total += seat_id
    expected_total = get_expected_total(min_seat_id, max_seat_id)
    print(f"Total: {total}")
    print(f"Expected total: {expected_total}")
    return expected_total - total 
