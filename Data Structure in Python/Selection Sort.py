numbers = [30, 18, 70, 100, 20, 5, 10, 50, 8, 14, 47]


def sort():
    for minimum in range(0, len(numbers)):
        for c in range(minimum + 1, len(numbers)):
            if numbers[c] < numbers[minimum]:
                temporary = numbers[minimum]
                numbers[minimum] = numbers[c]
                numbers[c] = temporary
print(numbers)
