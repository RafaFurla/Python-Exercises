from merge import merge


def mergesort(vector, left, right):
    if left >= right:
        return
    else:
        middle = ((left + right) // 2)
        mergesort(vector, left, middle)
        mergesort(vector, middle + 1, right)
        merge(vector, left, middle, right)


v1 = [10, 20, 30, 40, 50, 60, 5, 15, 25, 35, 45]
mergesort(v1, 0, len(v1))
print(v1)

