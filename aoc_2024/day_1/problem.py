from collections import defaultdict


def make_lists(text: str) -> tuple[list[int], list[int]]:
    text_lines = text.strip().split("\n")
    unzipped_lists = []
    for line in text_lines:
        a, b = line.split("   ")
        unzipped_lists.append([int(a), int(b)])
    return zip(*unzipped_lists)


def sort_and_compare(list_a: list[int], list_b: list[int]) -> int:
    list_a, list_b = sorted(list_a), sorted(list_b)
    diffs = [abs(a - b) for a, b in zip(list_a, list_b)]
    return sum(diffs)


def similarity_score(list_a: list[int], list_b: list[int]) -> int:
    list_b_counts = defaultdict(int)
    for i in list_b:
        list_b_counts[i] += 1

    score = 0
    for i in list_a:
        score += i * list_b_counts[i]
    return score
