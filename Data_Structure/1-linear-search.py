def linear_search(list_, number):
    for i in list_:
        if i == number:
            return print(f"The list has the number {number} locate in the position {list_.index(number)}")
    return print(f"The list doesn't contain the number {number}")


lis = [2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(lis, 10)

