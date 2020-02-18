def get_change(m):
    count = 0
    for i in [10, 5, 1]:
        x = int(m / i)
        count += x
        m = m - x * i
        if m == 0:
            break
    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
