from merge import merge


def mergesort(vector, left, right):
    if left >= right:
        return
    else:
        if len(vector[left:right+1]) % 2 == 0:
            middle = ((len(vector[left:right+1])//2)-1)+left
        else:
            middle = (len(vector[left:right+1])//2)+left
        mergesort(vector, left, middle)
        mergesort(vector, middle + 1, right)
        merge(vector, left, middle, right)

v1 = [10, 20, 30, 40, 50, 60, 5, 15, 25, 35, 45]
mergesort(v1, 0, 10)
print(v1)

