a = []
for c in range (1, 6, 1):
    a.append(int(input("Input an integer number on the list: ")))
print(f"The list is = {a}")
print("Now we will insert a new element in the first position of the list. The number 1000: ")
a.insert(0, 1000)
print(f"Our new list is: {a}")
print("If we delete the third element os the list this will result in: ")
a.pop(2)
print(a)
print("Now let's order the elements of the list: ")
a.sort()
print(a)
print("Now let's order the list in a decrease way: ")
a.sort(reverse=True)
print(a)
print(f"The list has {len(a)} elements.")
b = []
b = a
c = a[:]
print(f"b = a | b = {b}")
print(f"c = a[:] | c = {c}")
a[3] = 78
print(f"a[3] = 78 | a = {a} | b = {b} | c = {c}")
d = list(range(25, 80, 5))
print(f"New list: d = {d}")
a.append(d[:])
print(f"a.append(d[:])\na = {a}")

