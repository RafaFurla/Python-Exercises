def pa_soma(a1, r, n):
    if n < 1:
        return 0
    else:
        s = a1 + (n-1)*r
        return s + pa_soma(a1, r, n-1)


a1 = int(input("Define the first term of the arithmetic progression: "))
r = int(input("Define the reason of the arithmetic progression: "))
n = int(input("Define the number of therms of the arithmetic progression: "))
print(f"The sum of the terms of the A.P is: {pa_soma(a1, r, n)}")

