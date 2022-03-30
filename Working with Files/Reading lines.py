# 3 methods for read lines in a file:
print('################ Readline ################')
file = open(r'C:\Users\rafaf\Desktop\Test Python.txt')
print(file.readline())  # reading the first line
print(file.readline())  # reading the second line
print(file.readline())  # reading the third line
file.close()
print('################ Readlines ################')
file = open(r'C:\Users\rafaf\Desktop\Test Python.txt')
print(file.readlines())  # reading the first line
file.close()
print('')
print('')
print(' # ' * 30)
print('################ Readline ################')
file = open(r'C:\Users\rafaf\Desktop\Test Python.txt')
for line in file.readline():
    print(line)
file.close()
print('################ Readlines ################')
file = open(r'C:\Users\rafaf\Desktop\Test Python.txt')
for line in file.readlines():
    print(line)
file.close()
print('')
print('')
print(' # ' * 30)
file = open(r'C:\Users\rafaf\Desktop\Test Python.txt')
for line in file:
    print(line)
file.close()
