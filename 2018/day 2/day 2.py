day_1_example = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""


def preprocess_input(in_str):
    """
    Converts lines of text into a list of text. Strips empty lines
    :param in_str:
    :return:
    """
    return [x.strip() for x in in_str.strip('\n').split('\n')]


def check_chars(s):
    found_two_chars = False
    found_three_chars = False
    for c in set(s):
        found_two_chars = found_two_chars or s.count(c) == 2
        found_three_chars = found_three_chars or s.count(c) == 3
        if found_two_chars and found_three_chars:
            return True, True
    return found_two_chars, found_three_chars


def day_1_a(in_str):
    list_s = preprocess_input(in_str)
    two_char_count, three_char_count = 0, 0
    for s in list_s:
        found_two_chars, found_three_chars = check_chars(s)
        two_char_count += 1 if found_two_chars else 0
        three_char_count += 1 if found_three_chars else 0
    return two_char_count * three_char_count


assert day_1_a(day_1_example) == 12
with open("day 2.input") as f:
    print(day_1_a(f.read()))


day_1_b_example = """
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""


def get_common_letters(a, b):
    common_letters = ""
    for c1, c2 in zip(a, b):
        if c1 == c2:
            common_letters += c1
    return common_letters


def day_1_b(in_str):
    list_s = preprocess_input(in_str)
    for a in list_s:
        for b in list_s:
            if a == b:
                continue
            common_letters = get_common_letters(a, b)
            if len(a) - len(common_letters) == 1:
                return common_letters


assert day_1_b(day_1_b_example) == "fgij"
with open("day 2.input") as f:
    print(day_1_b(f.read()))
