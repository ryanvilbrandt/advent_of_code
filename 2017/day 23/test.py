
def main():
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = -1
    h = 0

    b = 93
    c = b
    if a != 0:
        b *= 100
        b += 100000
        c = b
        c += 17000
    print(locals())

    while True:

        # f = 1
        # d = 2
        #
        # # while g != 0:
        # while d != b:
        #     print(locals())
        #     e = 2
        #     # while g != 0:
        #     while e != b:
        #         # g = d
        #         # g *= e
        #         # g -= b
        #         if d * e == b:
        #             f = 0
        #         e += 1
        #         # g = e
        #         # g -= b
        #
        #     d = b
        #     # g = d
        #     # g -= b
        #
        # print(locals())
        # if f == 0:
        if is_prime_number(b):
            h += 1
        g = b
        g -= c
        if g == 0:
        # if b == c:
            return h
        b += 17


def is_prime_number(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def main2():
    primes = 0
    b = 100000 + 93 * 100
    c = b + 17000
    while not b == c:
        if is_prime_number(b):
            primes += 1
        b += 17
    return primes


if __name__ == "__main__":
    print(main2())
