# Uses python3
# import sys

def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a * b


def gcd(a, b):
    m = min(a, b)
    x = max(a, b)
    mod = x % m
    # print(mod)
    if mod == 0:
        return m
    return gcd(mod, m)


# lcm for 27[3*3*3] 12[3*2*2] = 108[27*2*2] or [27 * 12/gcm(3)]
def lcm(a, b):
    x = max(a, b)
    m = min(a, b)
    # corner cases
    if m == 0:
        return m
    if x % m == 0:
        return x
    # solution
    g = gcd(a, b)
    return int(x * m / g)


if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))
    print(lcm(a, b))
