def insertion_sort(vector):
    for i in range(1, len(vector)):
        j = i
        while (j>0) and (vector[j-1]>vector[j]):
            aux = vector[j]
            vector[j] = vector[j-1]
            vector[j-1] = aux
            j -= 1


v = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(v)
print(v)

