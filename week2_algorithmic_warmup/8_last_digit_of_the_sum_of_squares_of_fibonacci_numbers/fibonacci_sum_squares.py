def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


# why not square pisano of 10 = 60 / 60**2 = 360
def fibonacci_sum_squares(n):
    return fibonacci_sum_squares_naive(n % 360)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))
