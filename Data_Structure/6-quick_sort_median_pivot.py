from random import randint


def lomuto(v, left, right):
    pivot_index = pickpivotindex(v, left, right)
    save = v[pivot_index]
    v[pivot_index] = v[left]
    v[left] = save
    i = left
    for j in range(left+1, right+1):
        if v[j] <= v[left]:
            save = v[j]
            i += 1
            v[j] = v[i]
            v[i] = save
    save = v[i]
    v[i] = v[left]
    v[left] = save
    return i


def pickpivotindex(v, left, right):
    mid = (left+right)//2
    sort_ = [v[left], v[mid], v[right]]
    sort_ = sorted(sort_)
    if (sort_[1] == v[left]):
        return left
    elif (sort_[1] == v[mid]):
        return mid
    else:
        return right


def quicksort(v, pivot, right):
    if pivot < right:
        index_pivot = lomuto(v, pivot, right)
        quicksort(v, pivot, index_pivot-1)
        quicksort(v, index_pivot+1, right)


vector = [7, 12, 10, 8, 5, 19, 3, 90, 12, 85, 76]
quicksort(vector, 0, len(vector)-1)
print(vector)

