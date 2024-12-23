from collections import defaultdict
from functools import cmp_to_key

Rules = dict[int, list[int]]


def get_middle_page_sum(text_list: list[str]) -> int:
    rules, page_lists = get_rules_and_page_lists(text_list)
    sum = 0
    for page_list in page_lists:
        # print(page_list)
        if check_pages(rules, page_list):
            # print("Good!")
            sum += get_middle_page(page_list)
    return sum


def get_rules_and_page_lists(text_list: list[str]) -> tuple[Rules, list[list[int]]]:
    """
    Returns a dict of rules and a list of pages, parsed from the input text.
    The rules dict includes an entry for each page rule, with the value being every page that MUST come AFTER the key.
    """
    rules = defaultdict(list)
    pages = []
    for line in text_list:
        if not line:
            continue
        elif "|" in line:
            a, b = line.split("|")
            a, b = int(a), int(b)
            rules[a].append(b)
        else:
            pages.append([int(c) for c in line.split(",")])
    return rules, pages


def check_pages(rules: Rules, pages: list[int]) -> bool:
    checked_pages = set()
    for page in pages:
        # Get list of pages that must come after the current page
        page_rules = rules[page]
        # Check if any of those pages have already been checked
        invalid_pages = checked_pages.intersection(page_rules)
        if invalid_pages:
            # If any pages have come before this one, but the rules say they must come after, fail.
            return False
        # Add current page to checked pages
        checked_pages.add(page)
    return True


def get_middle_page(pages: list[int]):
    assert len(pages) % 2 == 1
    return pages[int(len(pages) / 2)]


def fix_pages_and_get_sum(text_list: list[str]) -> int:
    rules, page_lists = get_rules_and_page_lists(text_list)
    sum = 0
    for page_list in page_lists:
        # print(page_list)
        if not check_pages(rules, page_list):
            # print("Good!")
            fixed_pages = fix_pages(rules, page_list)
            sum += get_middle_page(fixed_pages)
    return sum


def fix_pages(rules: Rules, pages: list[int]):
    """
    Sorts a list of pages based on the precedency-rules.
    """
    def cmp(a, b):
        if a == b:
            return 0
        if b in rules[a]:
            return -1
        return 1
    return sorted(pages, key=cmp_to_key(cmp))