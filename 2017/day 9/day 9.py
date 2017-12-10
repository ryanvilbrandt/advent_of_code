import re

REG_NOT = re.compile(r"!.")
REG_GARBAGE = re.compile(r"<.*?>")

def count_groups(text):
    # print()
    # print("Text:", text)
    text = re.sub(REG_NOT, "", text)
    garbage_characters = re.findall(r"<(.*?)>", text)
    garbage_count = len("".join(garbage_characters))

    text = re.sub(REG_GARBAGE, "", text)
    # print("Cleaned text:", text)

    level = 0
    score = 0
    groups = 0

    for c in text:
        if c == "{":
            groups += 1
            level += 1
            score += level
        elif c == "}":
            level -= 1
    # print("Groups:", groups)
    assert level == 0
    return garbage_count, score

print(count_groups("<>"))
print(count_groups("<random characters>"))
print(count_groups("<<<<>"))
print(count_groups("<{!>}>"))
print(count_groups("<!!>"))
print(count_groups("<!!!>>"))
print(count_groups('<{o"i!a,<{i<a>'))
#
# print(count_groups("{}"))
# print(count_groups("{{{}}}"))
# print(count_groups("{{},{}}"))
# print(count_groups("{{{},{},{{}}}}"))
# print(count_groups("{<{},{},{{}}>}"))
# print(count_groups("{<a>,<a>,<a>,<a>}"))
# print(count_groups("{{<a>},{<a>},{<a>},{<a>}}"))
# print(count_groups("{{<!>},{<!>},{<!>},{<a>}}"))

# print(count_groups("{}"))
# print(count_groups("{{{}}}"))
# print(count_groups("{{},{}}"))
# print(count_groups("{{{},{},{{}}}}"))
# print(count_groups("{<a>,<a>,<a>,<a>}"))
print(count_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
print(count_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
print(count_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}"))

with open("day 9.input") as f:
    print(count_groups(f.read()))
