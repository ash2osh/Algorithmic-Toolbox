import itertools


def part(A):
    if sum(A) % 3 != 0:
        return 0
    share = int(sum(A) / 3)
    # get first one
    return part3(A, share)


def part3(A, share):
    for i in range(1, len(A)):
        items = [A[0]]
        for j in range(i, len(A)):
            if sum(items) == share:
                return items
            elif sum(items) > share:
                break
            items.append(A[j])

    return []


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


if __name__ == '__main__':
    n = input()
    A = list(map(int, input().split()))
    print(partition3(A))
    print(part(A))
