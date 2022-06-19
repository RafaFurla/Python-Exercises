def sort(list_):
    """
    This function is a selection sort algorithm. It will put a list in numerical order.
    :param list_: a list
    :return: a list ordered by numerial order.
    """

    for minimum in range(0, len(list_)):
        for c in range(minimum + 1, len(list_)):
            if list_[c] < list_[minimum]:
                temporary = list_[minimum]
                list_[minimum] = list_[c]
                list_[c] = temporary
    return list_


numbers = [30, 18, 70, 100, 20, 5, 10, 50, 8, 14, 47]
print(sort(numbers))
