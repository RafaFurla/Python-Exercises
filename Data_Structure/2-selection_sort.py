def selection_sort(vector):
    for i in range(0, len(vector)):
        i_smaller = i
        for j in range(i+1, len(vector)):
            if vector[j] < vector[i_smaller]:
                i_smaller = j
        aux = vector[i_smaller]
        vector[i_smaller] = vector[i]
        vector[i] = aux


v = [100,25,15,10,25]
selection_sort(v)
print(v)

