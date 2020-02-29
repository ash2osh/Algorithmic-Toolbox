def edit_distance(s, t):
    db[(0, 0)] = 0
    ls = len(s)
    lt = len(t)
    for i in range(1, ls + 1):
        db[(i, 0)] = i
    for j in range(1, lt + 1):
        db[(0, j)] = j

    for i in range(1, ls + 1):
        for j in range(1, lt + 1):
            x = [db[(i, j - 1)] + 1, db[(i - 1, j)] + 1]
            if s[i - 1] == t[j - 1]:
                x.append(db[(i - 1, j - 1)])
            else:
                x.append(db[(i - 1, j - 1)] + 1)
            db[(i, j)] = min(x)

    return db[(ls, lt)]


if __name__ == "__main__":
    db = {}
    print(edit_distance(input(), input()))
