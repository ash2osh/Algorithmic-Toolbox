import random


def partition3(array, left, right):
    j = left
    x = array[j]
    c_equal = 0  # number of equal elements
    for i in range(left + 1, right + 1):
        if array[i] < x:
            j += 1
            array[i], array[j] = array[j], array[i]
        elif array[i] == x:
            j += 1
            c_equal += 1  # count equals
            array[i], array[j] = array[j], array[i]  # switch i , j
            array[j], array[left + c_equal] = array[left + c_equal], array[
                j]  # switch j , left +count to put it near its equal

    for i in range(0, c_equal + 1):
        array[left + i], array[j - i] = array[j - i], array[left + i]
    return [j, c_equal]


def partition2(array, left, right):
    x = array[left]
    j = left
    for i in range(left + 1, right + 1):  # python stops at right
        if array[i] <= x:
            j += 1
            # switch i , j places because i value is smaller
            array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]
    return j


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    # switch left with random int !?
    array[left], array[k] = array[k], array[left]
    # m = partition2(array, left, right)
    p3 = partition3(array, left, right)
    m = p3[0]
    cnt = p3[1]
    randomized_quick_sort(array, left, m - cnt)
    randomized_quick_sort(array, m + 1, right)


def randomized_quick_sort_x(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort_x(a, l, m - 1);
    randomized_quick_sort_x(a, m + 1, r);


def print_array(array):
    for x in array:
        print(x, end=' ')


def test_large():
    for n in (10, 100, 10 ** 5):
        for max_value in (1, 2, 10, 10 ** 5):
            array = [random.randint(0, max_value) for _ in range(n)]
            original = array.copy()
            sorted_array = sorted(list(array))
            randomized_quick_sort(array, 0, len(array) - 1)
            if sorted_array != array:
                print_array(original)
                print()
                print_array(sorted_array)
                print()
                print_array(array)
                return


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    # elementsx = elements.copy()
    randomized_quick_sort(elements, 0, input_n - 1)
    print_array(elements)
#
# test_large()
# print()
# randomized_quick_sort_x(elementsx, 0, input_n - 1)
# for x in elementsx:
#     print(x, end=' ')
#
# if elements != sorted(elementsx):
#     print('NOT Equal ??')
