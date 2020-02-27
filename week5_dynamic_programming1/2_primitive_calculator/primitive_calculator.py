def optimal_sequence_rec(n):
    operations = []
    minOperations = []
    if n == 1:
        return [1]
    elif n <= 0:
        return [-1]

    for i in [1, 2, 3]:
        x = []
        if i == 1:
            next_n = n - 1
        elif n % i == 0:
            next_n = n // i
        else:
            next_n = n - 1
        if next_n == 1:
            x.append(n)
            x.append(1)
        elif next_n < n:
            x.append(n)
            x.extend(optimal_sequence(next_n))
        if -1 not in x:  # dos not contain -1
            operations.append(x)
    if len(operations) > 0:
        minOperations += min(operations, key=len)  # https://stackoverflow.com/questions/18741633
    return minOperations


def optimal_sequence_greedy(n):
    sq = []
    while n >= 1:
        sq.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sq)


def print_array(array):
    for x in array:
        print(x, end=' ')


input_n = int(input())
sequence = list(optimal_sequence_greedy(input_n))
print(len(sequence) - 1)
print_array(sequence)
print()
print_array(reversed(optimal_sequence_rec(input_n)))
