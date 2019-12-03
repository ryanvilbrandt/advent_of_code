from typing import Union, List


def intcode_parser(intcode: Union[List[int], str]):
    if isinstance(intcode, str):
        intcode = list(map(int, intcode.split(",")))
    i = 0
    while True:
        if intcode[i] == 99:
            return intcode
        a, b = intcode[intcode[i + 1]], intcode[intcode[i + 2]]
        if intcode[i] == 1:
            c = a + b
        elif intcode[i] == 2:
            c = a * b
        else:
            raise Exception("HALT AND CATCH FIRE")
        intcode[intcode[i + 3]] = c
        i += 4


assert intcode_parser("1,9,10,3,2,3,11,0,99,30,40,50") == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
assert intcode_parser("1,0,0,0,99") == [2, 0, 0, 0, 99]
assert intcode_parser("2,3,0,3,99") == [2, 3, 0, 6, 99]
assert intcode_parser("2,4,4,5,99,0") == [2, 4, 4, 5, 99, 9801]
assert intcode_parser("1,1,1,4,99,5,6,0,99") == [30, 1, 1, 4, 2, 5, 6, 0, 99]

with open("day 2 a.input") as f:
    s = f.read()

intcode = list(map(int, s.split(",")))
intcode[1] = 12
intcode[2] = 2
output = intcode_parser(intcode)
print(output[0])


def find_noun_verb(s):
    target_value = 19690720
    original_intcode = list(map(int, s.split(",")))
    for x in range(100):
        for y in range(100):
            intcode = original_intcode[:]
            intcode[1] = x
            intcode[2] = y
            output = intcode_parser(intcode)
            if output[0] == target_value:
                return x * 100 + y


print(find_noun_verb(s))
