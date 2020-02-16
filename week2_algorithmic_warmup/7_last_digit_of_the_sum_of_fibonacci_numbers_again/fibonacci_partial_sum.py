def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next = 1
    for i in range(to + 1):
        if i >= from_:
            sum += current
        current, next = next, current + next
    return sum % 10


def calc_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(0, n - 1):
        a, b = b, a + b
    return b


def test_fibonacci_partial_sum(f, t):
    for i in range(1, f):
        for j in range(i, t + 1):
            na = fibonacci_partial_sum_naive(i, j)
            my = fibonacci_partial_sum(i, j)
            if na != my:
                print(i, j, '-->', na, ' === ', my)


def fibonacci_partial_sum_old(from_index, to_index):
    total = 0
    new_to = to_index % 60
    if new_to == 0:
        return 0
    for i in range(from_index % 60, new_to + 1):
        total += calc_fib(i)
    return total % 10


def fibonacci_partial_sum(from_index, to_index):
    new_from = from_index % 60
    rng = (to_index - from_index) % 60
    return fibonacci_partial_sum_naive(new_from, new_from + rng)


if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    # test_fibonacci_partial_sum(from_, to)
    # print(fibonacci_partial_sum_naive(from_, to))
    # print(fibonacci_partial_sum_old(from_, to))
    print(fibonacci_partial_sum(from_, to))
