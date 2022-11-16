try:
    a = int(input("Type a integer number between in the interval 0 to 10: "))
    if (a < 0) or (a > 10):
        raise ValueError
except ValueError:
    print("The value inputted is not a valid option!")
else:
    print(a)
finally:
    print("End")

