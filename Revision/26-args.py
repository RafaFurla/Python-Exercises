def sum_(*elements):
    s = 0
    for i in elements:
        s += i
    return s


S = sum_(1, 2, 3, 4, 5)
print(S)

