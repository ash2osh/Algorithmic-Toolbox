# Uses python3
# import sys

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


def get_fibonacci_huge(n, m):
    # find m period length

    # get fib mod length

    f = calc_fib(n % m)
    print(f)
    # then mod again by m
    return f % m


if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print("-->", get_fibonacci_huge_naive(n, m))
    print("-->", get_fibonacci_huge(n, m))
