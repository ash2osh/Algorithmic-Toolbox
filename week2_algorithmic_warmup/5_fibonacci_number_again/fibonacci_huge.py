def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    print(current)
    return current % m


def calc_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(0, n - 1):
        a, b = b, a + b
    return b


def try_find_pisano():
    for m in range(2, 9999):
        print(m, '-->', find_pisano(m))


# 2-3 3-8 4-6 5-20 6-24 7-16 8-12 9-33

def find_pisano(m):
    prev, current = 0, 1
    for i in range(1, m ** 2 + 1):
        prev, current = current, (prev + current) % m
        if current == 1 and prev == 0:
            return i


def get_fibonacci_huge(n, m):
    # find m period length
    p = find_pisano(m)
    # get fib mod length
    f = calc_fib(n % p)
    print(f)
    # then mod  by m
    return f % m


if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    # try_find_pisano()
    # print("-->", get_fibonacci_huge_naive(n, m))
    print("-->", get_fibonacci_huge(n, m))
