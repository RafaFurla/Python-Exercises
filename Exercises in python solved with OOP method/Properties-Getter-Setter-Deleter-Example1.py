# Author: https://www.geeksforgeeks.org/getter-and-setter-in-python/
class Geeks:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("getter method called")
        return self._age

    @age.setter
    def age(self, a):
        print("setter method called")
        self._age = a

    @age.deleter
    def age(self):
        del self._age


print('OUTPUT: ')
print('')
mark = Geeks()

mark.age = 10

print(mark.age)

del mark.age
