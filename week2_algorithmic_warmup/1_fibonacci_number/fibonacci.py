# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(0, n - 1):
        a, b = b, a + b
    return b
    # return calc_fib(n - 1) + calc_fib(n - 2)


n = int(input())
print(calc_fib(n))
