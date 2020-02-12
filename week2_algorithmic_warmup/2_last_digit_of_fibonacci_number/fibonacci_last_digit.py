# Uses python3
import sys


def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def get_fibonacci_last_digit_naive(n):
    return calc_fib(n) % 10


def get_fibonacci_last_digit(n):
    x = n % 60
    return calc_fib(x) % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # print(get_fibonacci_last_digit_naive(n))
    for i in range(0, 999999):
        if get_fibonacci_last_digit(i) != get_fibonacci_last_digit_naive(i):
            print("worng answer for :", i)
