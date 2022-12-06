def lomuto(v):
    i = 0
    j = i + 1
    save = 0
    for j in range(1, len(v)):
        if v[j] <= v[0]:
            i += 1
            save = v[i]
            v[i] = v[j]
            v[j] = save
    save = v[0]
    v[0] = v[i]
    v[i] = save


v = [7, 12, 10, 8, 5, 19, 3, 90, 12]
lomuto(v)
print(v)

