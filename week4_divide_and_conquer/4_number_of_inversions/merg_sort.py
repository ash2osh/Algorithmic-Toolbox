def mergeSort(myList):
    inversions = 0
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
                inversions += 1
            else:
                myList[k] = right[j]
                j += 1
                inversions += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
            inversions += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
            inversions += 1
    print(inversions)


# count numbers fro x to 11
def simple(x):
    if x > 10:
        return x
    return x + simple(x + 1)


def simple_loop(x):
    count = 0
    while x < 12:
        count += x
        x += 1
    return count


myList = [5, 3, 9, 2, 9]
mergeSort(myList)
print(myList)
print(simple(1))
print(simple_loop(1))