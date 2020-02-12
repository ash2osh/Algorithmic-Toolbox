import datetime


def gcd_naive(a, b):
    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d


# def gcd(a, b):
#     diff = abs(a - b)
#     if diff == 0:
#         return a
#     for d in range(1, diff + 1):
#         if (diff % d) != 0:
#             continue
#         if a % (diff / d) == 0 and b % (diff / d) == 0:
#             return int(diff / d)
#     # if all fails return 1
#     return 1


# def gcd(a, b):
#     m = min(a, b)
#     x = max(a, b)
#     mod = x % m
#     if mod == 0:
#         return m
#     # for d in range(x, 0, -1):
#     #     if a % d == 0 and b % d == 0:
#     #         return d
#     for d in range(1, mod + 1):
#         if (mod % d) != 0:
#             continue
#         if a % (mod / d) == 0 and b % (mod / d) == 0:
#             return int(mod / d)
#         # if all fails return 1
#     return 1

def gcd(a, b):
    m = min(a, b)
    x = max(a, b)
    mod = x % m
    print(mod)
    if mod == 0:
        return m
    return gcd(mod, m)


if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(datetime.datetime.now())
    # print(gcd_naive(a, b))
    print(datetime.datetime.now())
    print(gcd(a, b))
    print(datetime.datetime.now())
