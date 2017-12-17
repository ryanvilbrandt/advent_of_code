FACTOR_A = 16807
FACTOR_B = 48271
DIVIDEND = 2147483647


def generate_num(num, factor, comp=1):
    num = (num * factor) % DIVIDEND
    while num % comp != 0:
        num = (num * factor) % DIVIDEND
    return num


def run_generators(start_a, start_b, runs=5):
    runs = int(runs)
    # print("--Gen. A--  --Gen. B--")
    curr_a = start_a
    curr_b = start_b
    matches = 0
    for i in range(runs):
        if i % 1e5 == 0:
            print(f"{i} / {runs}")
        curr_a = generate_num(curr_a, FACTOR_A, 4)
        curr_b = generate_num(curr_b, FACTOR_B, 8)
        if curr_a & 0xFFFF == curr_b & 0xFFFF:
            matches += 1
        # print("{:>10}  {:>10}".format(curr_a, curr_b))
    return matches


# print(run_generators(65, 8921))
# print(run_generators(65, 8921, runs=40e6))
# print(run_generators(289, 629, runs=40e6))
# print(run_generators(65, 8921, runs=5e6))
print(run_generators(289, 629, runs=5e6))