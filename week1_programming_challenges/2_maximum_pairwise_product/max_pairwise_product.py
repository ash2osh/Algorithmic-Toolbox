# python3
# from random import seed
from random import randint


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    max_product = max1 * max2

    return max_product


def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product


def randInt(n):
    return randint(0, 10 ** n)


def stress_test():
    nums = []
    for i in range(0, 50):
        nums.append(randInt(4))
    fast = max_pairwise_product(nums.copy())
    slow = max_pairwise_product_slow(nums.copy())

    if fast == slow:
        print("ok result", fast, " for ", nums)
    else:
        print("bad result fast: ", fast, "slow:", slow, " for ", nums)


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    # for _ in range(0, 10 ** 5):
    #     stress_test()
