# no repetition is enabled
# cases
# (10, (1, 4, 8), 9),
# (20, (5, 7, 12, 18), 19),
# (10, (3, 5, 3, 3, 5), 10),


def optimal_weight(knapsack, weights):
    if knapsack <= 0:
        return 0
    if (knapsack, tuple(weights)) in db:
        return db[(knapsack, tuple(weights))]
    for i in range(1, knapsack + 1):
        mx = 0
        mxLst = []
        for g in weights:
            if g <= i:
                new_weights = weights.copy()
                new_weights.remove(g)
                mxLst.append(g + optimal_weight(i - g, new_weights))
        if len(mxLst) > 0:
            mx = max(mxLst)
        db[(i, tuple(weights))] = mx

    return db[(knapsack, tuple(weights))]


# this is the solution if repetitions was enabled
# def optimal_weight_with_repetition(knapsack, weights):
#     if knapsack <= 0:
#         return 0
#     if knapsack in db:
#         return db[knapsack]
#     for i in range(1, knapsack + 1):
#         mx = 0
#         mxLst = []
#         for g in weights:
#             if g <= i:
#                 new_weights = weights.copy()
#                 # new_weights.remove(g) # dont remove for repetitions solution
#                 mxLst.append(g + optimal_weight_with_repetition(i - g, new_weights))
#         if len(mxLst) > 0:
#             mx = max(mxLst)
#         db[i] = mx
#
#     return db[knapsack]


if __name__ == '__main__':
    W, n = list(map(int, input().split()))
    w = list(map(int, input().split()))
    db = {}
    # print(W, n, w)
    print(optimal_weight(W, w))
