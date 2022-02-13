n = int(input('Input a integer number: '))
t = int(1)
s = ma = me = int(n)
r = str(input('Do you want to continue? [Y]/[N] ')).strip().upper()
while r != 'N':
    n = int(input('Input a integer number: '))
    t += 1
    s += n
    if n > ma:
        ma = n
    if n < me:
        me = n
    r = (input('Do you want to continue? [Y]/[N] ')).strip().upper()
print('''The average of the input numbers is: {}
The biggest number is: {}
The lowest number is: {}'''.format(s / t, ma, me))
