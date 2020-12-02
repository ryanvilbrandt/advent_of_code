class NoRegexMatch(Exception):
    pass


def text_to_list(text):
    for line in text.strip("\n ").split("\n"):
        yield line.strip(" ")
