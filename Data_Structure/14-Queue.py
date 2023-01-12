class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        """insert an element to the Queue"""
        node = Node(elem)
        if self.last is None:  # covers the case when the Queue doesn't have any element
            self.last = node
        else:  # covers the case when the Queue has at least one element.
            self.last.next = node  # this conects the last element (before the insertion) with the new element inserted.
            self.last = node  # put the element inserted in the last position.
        if self.first is None:
            self.first = node
        self._size += 1

    def pop(self):
        """removes the element in the top of the Queue"""
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        else:
            print("The queue is empty")

    def peek(self):
        """returns the more ancient element of the Queue. That that occupies the first position"""
        if self._size > 0:
            elem = self.first.data
            return elem
        else:
            print("The queue is empty!")

    def __len__(self):
        """this function serves to say how many elements are in the Queue"""
        return self._size

    def __repr__(self):
        """returns the representation of an object of the Queue class when the user calls the print function for the object"""
        if self._size > 0:
            r = ""
            pointer = self.first
            while pointer:
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        else:
            return "Empty Queue"

    def __str__(self):
        """this function explains how to do the conversion of an object of the Queue class into a string"""
        return self.__repr__()

fila = Queue()
print(fila)
fila.push(5)
fila.push(9)
fila.push("Hallison")
fila.push(True)
fila.push(42)
print(fila)
fila.pop()
fila.pop()
fila.pop()
fila.pop()
fila.pop()
fila.pop()
fila.push(5)
fila.push(6)
print(fila)
print(f'Tamanho da fila: {len(fila)}')
print(f'Último mais antigo da fila: {fila.peek()}')

