import re
from typing import Any


def text_to_list(text: str):
    for line in text.strip("\n ").split("\n"):
        yield line.strip(" ")


def text_to_grid(text: str, delimiter: str = "", convert: callable = str) -> list[list[Any]]:
    for line in text_to_list(text):
        if not delimiter:
            yield list(line)
        else:
            yield [convert(item) for item in re.split(r"\s+", line)]
