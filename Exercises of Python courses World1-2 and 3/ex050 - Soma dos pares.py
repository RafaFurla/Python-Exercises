s = int(0)
for c in range(1, 7):
    n = int(input('Input a integer number: '))
    if n % 2 == 0:
        s = s + n
print('The add of the even numbers is: {}'.format(s))
