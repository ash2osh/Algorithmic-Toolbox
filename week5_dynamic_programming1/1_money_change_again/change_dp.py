# dynamic programing solution
def get_change(money):
    if money == 0:
        return 0
    elif money < 0:
        return -1
    minChange = 0
    min_changes = []
    for i in [1, 3, 4]:
        next_money = money - i
        if next_money == 0:  # path ends here
            min_changes.append(1)
        elif next_money > 0:
            x = 1
            if next_money in db:
                x += db[next_money]
            else:
                x += get_change(next_money)
            if x > 0:  # remove negative paths
                min_changes.append(x)
    if len(min_changes) > 0:
        minChange += min(min_changes)
        db[money] = minChange
    return minChange


def get_change_rec(money):
    if money == 0:
        return 0
    elif money < 0:
        return -1
    minChange = 0
    changes = []
    for i in [1, 3, 4]:
        next_money = money - i
        if next_money == 0:  # path ends here
            changes.append(1)
        elif next_money > 0:
            x = 1
            x += get_change_rec(next_money)
            if x > 0:  # remove negative paths
                changes.append(x)
    if len(changes) > 0:
        minChange += min(changes)
        # z = minChange # for debug only

    return minChange


def get_change_greedy(money):
    change = 0
    for i in [4, 3, 1]:
        if money <= 0:
            return change
        change += money // i
        money = money % i

    return change


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


if __name__ == '__main__':
    n = int(input())
    db = {}
    print(get_change(n))
    # for m in range(0, n + 1):
    #     print(get_change_greedy(m))
    #     print(get_change(m))
    #     print(change_naive(m))
    #     print(get_change_rec(m))
    #     print(get_change(m))
    #     print()
