def sort(list):
    """
    This function is a selection sort algorithm and it will put a list in numerical order.
    :param list: a list
    :return: a list ordered by numerial order.
    """

    for minimum in range(0, len(list)):
        for c in range(minimum + 1, len(list)):
            if list[c] < list[minimum]:
                temporary = list[minimum]
                list[minimum] = list[c]
                list[c] = temporary
    return list


numbers = [30, 18, 70, 100, 20, 5, 10, 50, 8, 14, 47]
print(sort(numbers))
print(numbers)
