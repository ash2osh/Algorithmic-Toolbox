def binary_search_recursive(keys, mn, mx, query):
    md = int((mx - mn) / 2)
    if mx - mn <= 1:
        if query == keys[mn]:
            return mn
        elif query == keys[mx]:
            return mx
        else:
            return -1
    if query == keys[md]:
        return md
    elif query > keys[md]:
        return binary_search_recursive(keys, md + 1, mx, query)
    elif query < keys[md]:
        return binary_search_recursive(keys, mn, md - 1, query)
    return -1


def binary_search(keys, query):
    mn, mx = 0, len(keys)-1
    while 1:
        md =


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    mn, mx = 0, len(input_keys) - 1
    for q in input_queries:
        print(linear_search(input_keys, q), end=' ')

    print()
    for q in input_queries:
        print(binary_search_recursive(input_keys, mn, mx, q), end=' ')

    # print()
    # for q in input_queries:
    #     print(binary_search(input_keys, q), end=' ')
# input
#

# 5 1 2 3 4 5
# out
# 0 1 2 3 4
