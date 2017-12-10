def normalize_list(mylist, index):
    """
    Rearranges the list such that the current index is the start of the list.
    :param mylist:
    :param index:
    :return:
    """
    return mylist[index:] + mylist[:index]

def reverse_chunk(mylist, length):
    """
    Assumes a normalized list. Reverses the first N characters in the list.
    :param mylist:
    :param length:
    :return:
    """
    return list(reversed(mylist[:length])) + mylist[length:]

# def tie_knot(mylist, lengths):
#     current_index = 0
#     skip_size = 0
#     for n in lengths:
#         mylist = reverse_chunk(mylist, n)
#         current_index = (current_index + n + skip_size) % len(mylist)
#         mylist = normalize_list(mylist, (n + skip_size) % len(mylist))
#         print(mylist)
#         skip_size += 1
#     current_index -= 1
#     mylist = normalize_list(mylist, current_index)
#     print(mylist)
#     return mylist, current_index, skip_size


# r = list(range(5))
# n = tie_knot(r, [3, 4, 1, 5])
# print(n[0] * n[1])
#
# r = list(range(256))
# n = tie_knot(r, [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144])
# print(n[0] * n[1])


def tie_knot(mylist, lengths, current_index=0, skip_size=0):
    for n in lengths:
        mylist = reverse_chunk(mylist, n)
        current_index = (current_index + n + skip_size) % len(mylist)
        mylist = normalize_list(mylist, (n + skip_size) % len(mylist))
        print(mylist)
        skip_size += 1
    return mylist, current_index, skip_size

SUFFIX = "\x17\x31\x73\x47\x23"

def calc_hash(myinput, rounds=64, suffix=SUFFIX, list_length=256):
    print(myinput)
    mylist = list(range(list_length))
    myinput += suffix
    lengths = [ord(c) for c in myinput]

    current_index = 0
    skip_size = 0
    for r in range(rounds):
        mylist, current_index, skip_size = tie_knot(mylist, lengths, current_index, skip_size)
    # Convert list to original orientation
    mylist = normalize_list(mylist, current_index * -1)
    print(mylist)

    def xor_chunk(chunk):
        x = 0
        for n in chunk:
            x ^= n
        return x
    num_hash = [xor_chunk(mylist[x:x+16]) for x in range(0, 256, 16)]
    return "".join("{:>02x}".format(c) for c in num_hash)

assert calc_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
