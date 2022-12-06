def lomuto(v, pivot, right):
    i = pivot
    for j in range(pivot+1, right+1):
        if v[j] <= v[pivot]:
            salve = v[j]
            i += 1
            v[j] = v[i]
            v[i] = salve
    salve = v[i]
    v[i] = v[pivot]
    v[pivot] = salve
    return i


def quicksort(v, pivot, right):
    if pivot < right:
        index_pivot = lomuto(v, pivot, right)
        quicksort(v, pivot, index_pivot-1)
        quicksort(v, index_pivot+1, right)


vector = [7, 12, 10, 8, 5, 19, 3, 90, 12, 85, 76]
quicksort(vector, 0, len(vector)-1)
print(vector)

