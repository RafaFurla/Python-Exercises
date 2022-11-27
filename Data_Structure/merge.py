def merge(vector, left, middle, right):
    helper = list()
    for c in range(0, len(vector)):
        helper.append(vector[c])
    i = left
    j = middle + 1
    k = left
    while (i <=middle) and (j < right):
        if helper[i] < helper[j]:
            vector[k] = helper[i]
            i += 1
            k += 1
        else:
            vector[k] = helper[j]
            j += 1
            k += 1
    while i <= middle:
        vector[k] = helper[i]
        i += 1
        k += 1
    while j < right:
        vector[k] = helper[j]
        j += 1
        k += 1

