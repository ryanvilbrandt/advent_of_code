from typing import List


def find_match(num_list: List[int]):
    list_length = len(num_list)
    for i in range(list_length):
        for j in range(i + 1, list_length):
            if num_list[i] + num_list[j] == 2020:
                return num_list[i] * num_list[j]
    return None


def find_three_match(num_list: List[int]):
    list_length = len(num_list)
    for i in range(list_length):
        for j in range(i + 1, list_length):
            for k in range(j + 1, list_length):
                if num_list[i] + num_list[j] + num_list[k] == 2020:
                    return num_list[i] * num_list[j] * num_list[k]
    return None
