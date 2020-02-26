def partition2(array, left, right):
    x = array[left]
    j = left
    count = 0
    for i in range(left + 1, right + 1):  # python stops at right
        if array[i] <= x:
            j += 1
            # switch i , j places because i value is smaller
            array[i], array[j] = array[j], array[i]
            count += 1
    array[left], array[j] = array[j], array[left]
    return [j, count]


def get_number_of_inversions(array, left, right):
    number_of_inversions = 0
    if left >= right:
        return number_of_inversions
    m = partition2(array, left, right)
    number_of_inversions += m[1]
    # ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(array, left, m[0] - 1)
    number_of_inversions += get_number_of_inversions(array, m[0] + 1, right)
    # write your code here
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    # n, *a = list(map(int, input().split()))
    # b = input_n * [0]  # empty array of 0
    print(get_number_of_inversions(elements, 0, input_n - 1))
    print(elements)
