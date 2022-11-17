def yearmonth(func, arg):
    return (func(arg)-1)*100


print((lambda z: 2 * z)(4))
print(yearmonth(lambda x: (1+x/100)**(1/12), 4))

