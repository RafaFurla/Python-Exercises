def showline(msg="Example Message"):
    """Message decorator. Put a message in the parentheses and the function will decorate your message"""
    a = len(msg)+10
    print("=" * a)
    print(4 * " ", f"{msg:^0}", 4 * " ")
    print("=" * a)


def thesum(a=0, b=0):
    """Give you the sum of two numbers. Put 2 numbers in the parentheses """
    print(f"The sum of {a} + {b} is equal to: {a + b}")


def opensum(* num):
    """Return the sum of the numbers you typed in the parentheses when you call the function"""
    sum = int(0)
    for c in num:
        sum += c
    print(f"The sum of the inputed numbers is: {sum}")


def doublelist(lst):
    """Double the values on your list!"""
    for c in range(0, len(lst), 1):
        lst[c] = 2 * lst[c]


def doublenumber(x):
    global n
    n = n * 2


def returntest(a=0, b=0, c=0):
    r = ""
    sumtest = 0
    multest = 1
    while True:
        r = str(input("Type S to Sum or M to Multiply the number: ")).upper()
        if (r != "S") and (r != "M"):
            print(f"{r} is not a valid option")
        else:
            break
    if r == "S":
        sumtest = a + b + c
        return sumtest
    else:
        multest = a * b * c
        return multest


showline()
thesum(5, 6)
opensum(1, 2, 3, 4, 5)
test = [2, 3, 4, 5, 6]
doublelist(test)
print(test)
n = 3
doublenumber(n)
print(n)
test = returntest(1, 1, 1)
print(test)

