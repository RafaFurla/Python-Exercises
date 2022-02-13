'''n = int(input('input a integer number: '))
m = int(1)
while n != 0:
    m *= n
    n += -1
print('The factorial of the input number is: {}'.format(m))'''

n1 = int(input('Input a integer number: '))
mul = int(1)
for n1 in range(n1, 1, -1):
    mul *= n1
print('The factorial of the input number is: {}'.format(mul))
