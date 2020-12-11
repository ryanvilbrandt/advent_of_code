from typing import List


class NoRegexMatch(Exception):
    pass


def text_to_list(text):
    for line in text.strip("\n ").split("\n"):
        yield line.strip(" ")


def text_to_grid(text) -> List[List[str]]:
    return [list(line) for line in text_to_list(text)]
