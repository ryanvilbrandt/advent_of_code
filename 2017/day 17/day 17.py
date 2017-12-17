def spinlock(cycle, end=2017, find_value_after=2017):
    array = [0]
    index = 0
    for i in range(1, end + 1):
        if i % 1e4 == 0:
            print(f"{i} / {end}")
        index = (index + cycle) % len(array) + 1
        array.insert(index, i)
        # print(index, array)
    print(array[:10])
    return array[array.index(find_value_after) + 1]


def fast_spinlock(cycle, end=2017):
    last_insert = None
    array_size = 1
    index = 0
    for i in range(1, end + 1):
        if i % 1e6 == 0:
            print(f"{i} / {end}")
        index = (index + cycle) % array_size + 1
        if index == 1:
            last_insert = i
        array_size += 1
    return last_insert


# print(spinlock(3))
# print(fast_spinlock(3))
# print(spinlock(328))
# print(fast_spinlock(328))

print(fast_spinlock(328, end=int(50e6)))
