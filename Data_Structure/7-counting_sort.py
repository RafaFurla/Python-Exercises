def order(A):
    big, minor = bigger_minor(A)
    C = []
    B = []
    if minor >= 0:
        for i in range(0, big+1):
            C.append(0)
        for i in range(0, len(A)):
            B.append(0)
        for i in range(0, len(A)):
            C[A[i]] += 1
        for i in range(1, len(C)):
            C[i] = C[i] + C[i-1]
        for i in range(len(A)-1, -1, -1):
            B[C[A[i]]-1] = A[i]
            C[A[i]] -= 1
    else:
        for i in range(0, big+1+abs(minor)):
            C.append(0)
        for i in range(0, len(A)):
            B.append(0)
        for i in range(0, len(A)):
            C[A[i]+abs(minor)] += 1
        for i in range(1, len(C)):
            C[i] = C[i] + C[i-1]
        for i in range(len(A)-1, -1, -1):
            B[C[A[i]+abs(minor)]-1] = A[i]
            C[A[i]+abs(minor)] -= 1
    return B


def bigger_minor(A):
    big = minor = A[0]
    for i in range(1, len(A)):
        if A[i] > big:
            big = A[i]
    for i in range(1, len(A)):
        if A[i] < minor:
            minor = A[i]
    return big, minor


A = [0, 8, 1, 6, 2, 1, 12, 3, 5, 6, 0, -2, -3, -5]
print(order(A))

