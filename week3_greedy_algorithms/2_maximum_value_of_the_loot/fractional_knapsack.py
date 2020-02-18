def get_optimal_value(capacity, weights, values):
    result = 0.
    remainingCapacity = capacity
    prices = []
    for i in range(0, len(weights)):
        prices.append(values[i] / weights[i])

    for _ in range(0, len(weights)):
        # get max values and weights
        maxPrice = max(prices)
        maxIndex = prices.index(maxPrice)
        maxVal = values[maxIndex]
        maxWeight = weights[maxIndex]
        # remove those from arrays
        weights.pop(maxIndex)
        values.pop(maxIndex)
        prices.pop(maxIndex)
        # weights.remove(maxWeight)
        # values.remove(maxVal)
        if remainingCapacity - maxWeight >= 0:
            remainingCapacity = remainingCapacity - maxWeight
            result += maxVal
        else:
            result += remainingCapacity / maxWeight * maxVal
            remainingCapacity = 0
        if remainingCapacity == 0:
            break

    return result


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print(n, capacity, values, weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
