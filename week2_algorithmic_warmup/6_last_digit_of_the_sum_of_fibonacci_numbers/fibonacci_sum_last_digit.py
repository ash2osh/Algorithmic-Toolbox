# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def test_fibonacci_sum():
    for i in range(1, 50):
        print(i, '-->', fibonacci_sum_naive(i), ' === ', fibonacci_sum(i))


def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def fibonacci_sum_slow(n):
    if n <= 1:
        return n
    total = 1
    for i in range(2, n + 1):
        total += calc_fib(i % 60) % 10

    return total % 10


# must calc this in less than 1 sec 832564823476
def fibonacci_sum(n):
    return calc_fib(n % 60) % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    test_fibonacci_sum()
    # print(fibonacci_sum_naive(n))
    # print(fibonacci_sum(n))
