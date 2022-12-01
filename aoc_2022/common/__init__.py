from typing import List


def text_to_list(text: str):
    for line in text.strip("\n ").split("\n"):
        yield line.strip(" ")


def text_to_grid(text: str) -> List[List[str]]:
    return [list(line) for line in text_to_list(text)]
