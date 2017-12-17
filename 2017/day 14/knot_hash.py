SUFFIX = [17, 31, 73, 47, 23]


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


def tie_knot(mylist, lengths, current_index=0, skip_size=0):
    for n in lengths:
        mylist = reverse_chunk(mylist, n)
        current_index = (current_index + n + skip_size) % len(mylist)
        mylist = normalize_list(mylist, (n + skip_size) % len(mylist))
        skip_size += 1
    return mylist, current_index, skip_size


def calc_hash(myinput, rounds=64, suffix=SUFFIX, list_length=256):
    # print(myinput)
    mylist = list(range(list_length))
    lengths = [ord(c) for c in myinput]
    lengths += suffix

    current_index = 0
    skip_size = 0
    for r in range(rounds):
        mylist, current_index, skip_size = tie_knot(mylist, lengths, current_index, skip_size)
    # Convert list to original orientation
    mylist = normalize_list(mylist, current_index * -1)

    def xor_chunk(chunk):
        x = 0
        for n in chunk:
            x ^= n
        return x
    num_hash = [xor_chunk(mylist[x:x+16]) for x in range(0, 256, 16)]
    return "".join("{:>02x}".format(c) for c in num_hash)


# assert calc_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
# assert calc_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
# assert calc_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
# assert calc_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
# print(calc_hash("227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144"))
