def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def get_majority_element_divide(elements):
    m = int(len(elements) / 2)


def get_majority_element(elements):
    els = {}  # dictionary
    for e in elements:
        if e in els:
            els[e] = els[e] + 1
        else:
            els[e] = 1
    if max(els.values()) > len(elements) / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    print(majority_element_naive(input_elements))
    print(get_majority_element(input_elements))
    print(get_majority_element_divide(input_elements))
