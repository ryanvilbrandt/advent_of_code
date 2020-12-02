import re

from aoc_2020.common import NoRegexMatch, text_to_list


def check_password_part_1(line):
    m = re.match(r"(\d+)-(\d+) (.*?): (.*)", line)
    if not m:
        raise NoRegexMatch(line)
    minimum, maximum, character, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    character_count = password.count(character)
    return minimum <= character_count <= maximum


def check_passwords_part_1(text):
    results = [check_password_part_1(line) for line in text_to_list(text)]
    print(results)
    return sum(results)


def check_password_part_2(line):
    m = re.match(r"(\d+)-(\d+) (.*?): (.*)", line)
    if not m:
        raise NoRegexMatch(line)
    pos_1, pos_2, character, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    a = password[pos_1 - 1]
    b = password[pos_2 - 1]
    return (a == character) ^ (b == character)


def check_passwords_part_2(text):
    results = [check_password_part_2(line) for line in text_to_list(text)]
    print(results)
    return sum(results)
