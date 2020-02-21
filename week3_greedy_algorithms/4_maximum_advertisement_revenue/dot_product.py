def max_dot_product(a, b):
    res = 0
    for i in range(len(a)):
        ma = max(a)
        mb = max(b)
        res += ma * mb
        a.remove(ma)
        b.remove(mb)

    return res


if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
