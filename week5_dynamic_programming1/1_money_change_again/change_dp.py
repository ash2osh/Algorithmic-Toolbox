def get_change(money):
    # write your code here
    return money // 4


def get_change_rec(money):
    min_coin = 0
    # num1, num2, num3 = 0, 0, 0
    # num1, num2, num3 = {1: 0, 3: 0, 4: 0}, {1: 0, 3: 0, 4: 0}, {1: 0, 3: 0, 4: 0}
    num1 = 0
    if money <= 0:
        return 0
    num1 += 1
    money = money - 1
    num1 += get_change_rec(money)
    return num1


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
    m = int(input())
    print(get_change(m))
    print(get_change_greedy(m))
    print(change_naive(m))
    print(get_change_rec(m))
