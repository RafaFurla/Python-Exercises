def merge(vector_a, vector_b):
    a = 0
    b = 0
    vector_c = list()
    while (a < len(vector_a)) and (b < len(vector_b)):
        if vector_a[a] <= vector_b[b]:
            vector_c.append(vector_a[a])
            a += 1
        else:
            vector_c.append(vector_b[b])
            b += 1
    while a < len(vector_a):
        vector_c.append(vector_a[a])
        a += 1
    while b < len(vector_b):
        vector_c.append(vector_b[b])
        b += 1
    return vector_c


v1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20]
v2 = [2, 4, 6, 8, 10, 12, 14, 16]
v3 = merge(v2, v1)
print(v3)

