import random 

def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        meio = (begin + end) // 2
        if array[meio] == item:
            return meio
        if item < array[meio]:
            return binary_search(array, item, begin, meio-1)
        else:
            return binary_search(array, item, meio+1, end)
    return None

# ****************** Test ********************

empty = [1]
single = [7]
pair = [3, 7]
odd = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43]
even = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43, 70]
repeated = [1, 2, 2, 5, 5, 5, 9, 13, 21, 21, 21, 21]

def test_empty():
    if binary_search(empty, random.randint(0, 1000)) is not None:
        return False
    else:
        return True


def test_single():
    if binary_search(single, 7):
        return False
    if binary_search(single, 10) is not None:
        return False
    else:
        return True


print("****************************************************")
if test_empty():
    print("EMPTY CHECK")
else:
    print("EMPTY FAIL")
if test_single():
    print("UNIQUE CHECK")
else:
    print("UNIQUE FAIL")

test_cases = {"Pair": pair, "Odd": odd, "Even": even, "Repeated": repeated}
again = "s"
while again == "s":
    for name, lista in test_cases.items():
        print("\nTest Case: {}\n".format(name, lista))
        # select in the list
        e = int(input("Element that will be searched: "))
        i = binary_search(lista, e)
        print("\n Índice encontrado:", i)
    again = input("Repeat? (S/N): ").lower()
print("***************************************")


