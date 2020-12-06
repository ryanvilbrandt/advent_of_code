import re
from functools import reduce
from math import inf

from aoc_2020.common import text_to_list


# def get_all_yes_answers(answers):
#     return len(set(re.sub(r"[\n ]", "", answers)))


def get_all_yes_answers(answers):
    return len(reduce(
        lambda a, b: set(a).intersection(b),
        map(set, text_to_list(answers))
    ))


def get_all_answer_counts(all_answers):
    return [get_all_yes_answers(a) for a in all_answers.split("\n\n")]


def sum_answer_counts(all_answers):
    return sum(get_all_answer_counts(all_answers))
