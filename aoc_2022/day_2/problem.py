from typing import List, Tuple

from aoc_2022.common import text_to_list

my_score_map = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

their_score_map = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

win_map = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

score_map_v2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}


def score_round(theirs: str, mine: str) -> int:
    score = my_score_map[mine]
    if their_score_map[theirs] == my_score_map[mine]:
        return score + 3
    if mine == win_map[theirs]:
        return score + 6
    return score


def follow_strategy_guide(text):
    guide = text_to_list(text)
    score = 0
    for line in guide:
        theirs, mine = line.split(" ")
        score += score_round(theirs, mine)
    return score


def follow_strategy_guide_v2(text):
    guide = text_to_list(text)
    return sum(score_map_v2[line] for line in guide)
