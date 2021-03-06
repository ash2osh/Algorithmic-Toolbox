# no repetition is enabled
# cases
# (10, (1, 4, 8), 9),
# (20, (5, 7, 12, 18), 19),
# (10, (3, 5, 3, 3, 5), 10),
# 999 90
# 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100 10 20 30 40 50 60 70 80 90 100

# failed attempt
# def optimal_weight(knapsack, weights):
#     db[(0, 0)] = 0
#     # for i in range(1, knapsack + 1):
#     #     db[(i, 0)] = 0
#     for j in range(1, len(weights) + 1):
#         db[(0, j)] = 0
#     mx = 0
#     for i in range(1, knapsack + 1):
#         mx = 0
#         mxLst = []
#         for j in range(0, len(weights)):
#             if weights[j] <= i:
#                 new_weights = weights.copy()
#                 new_weights2 = weights.copy()
#                 new_weights.pop(j)
#                 if (i, j) in db:
#                     mxLst.append(weights[j] + db[(i, j)])
#                 else:
#                     z = weights[j] + optimal_weight(i - weights[j], new_weights)
#                     z2 = optimal_weight(weights[j], new_weights2)
#                     db[(i, j)] = max(z, z2)
#                     mxLst.append(db[(i, j)])
#
#             if len(mxLst) > 0:
#                 mx = max(mxLst)
#
#     return mx


# wrong answer
def optimal_weight(knapsack, weights):
    weights = [0] + weights
    items = len(weights)
    capacity = knapsack + 1

    # Create a matrix with initial values.
    matrix = [[0 for _ in range(items)] for _ in range(capacity)]

    for j in range(1, items):
        for i in range(1, capacity):
            prev = matrix[i][j - 1]
            if weights[j] == i:
                cur = weights[j]
            else:
                cur = weights[j] + matrix[knapsack - weights[j]][j - 1]
            if cur > i:
                matrix[i][j] = prev
            else:
                matrix[i][j] = max(prev, cur)

    return matrix[-1][-1]


def optimal_weight2(W, w):
    value = [[0]*(len(w)+1) for _ in range(W+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            value[j][i] = value[j][i-1]
            if w[i-1] <= j:
                val = value[j-w[i-1]][i-1] + w[i-1]
                if val >= value[j][i]:
                    value[j][i] = val
    return value[W][len(w)]



def optimal_weight_unique_rec(knapsack, weights):
    if knapsack <= 0:
        return 0
    if (knapsack, tuple(weights)) in db:
        return db[(knapsack, tuple(weights))]
    weights_range = sorted(i for i in weights if i < knapsack)
    weights_range.append(knapsack)
    for i in weights_range:
        mx = 0
        mxLst = []
        for g in weights:
            if g <= i:
                new_weights = weights.copy()
                new_weights.remove(g)
                mxLst.append(g + optimal_weight_unique_rec(i - g, new_weights))
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
    rec = 0
    lookup = 0
    # print(W, n, w)
    # print(optimal_weight(W, w))
    print(optimal_weight2(W, w))
    # print(optimal_weight_unique_rec(W, w))
